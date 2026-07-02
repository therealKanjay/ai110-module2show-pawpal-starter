import json
from datetime import datetime, date, time, timedelta
from typing import Any, Dict, List, Optional
from uuid import uuid4


# ============================================================================
# Data Models
# ============================================================================

class Pet:
    """Represents a pet in the system."""
    
    def __init__(
        self,
        name: str,
        gender: str,
        bodyWeight: float,
        petType: str,
        dateAdded: Optional[date] = None,
        petId: Optional[str] = None,
    ):
        """Initialize a new pet with the provided details."""
        self.petId: str = petId or str(uuid4())
        self.name: str = name
        self.gender: str = gender
        self.bodyWeight: float = bodyWeight
        self.petType: str = petType
        self.dateAdded: date = dateAdded or date.today()
        self.tasks: List[Task] = []

    @property
    def task_count(self) -> int:
        """Return the number of tasks assigned to the pet."""
        return len(self.tasks)

    def add_task(self, task: "Task") -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the pet into a serializable dictionary."""
        return {
            "petId": self.petId,
            "name": self.name,
            "gender": self.gender,
            "bodyWeight": self.bodyWeight,
            "petType": self.petType,
            "dateAdded": self.dateAdded.isoformat(),
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Pet":
        """Create a pet from a dictionary payload."""
        return Pet(
            name=data["name"],
            gender=data["gender"],
            bodyWeight=data["bodyWeight"],
            petType=data["petType"],
            dateAdded=date.fromisoformat(data["dateAdded"]),
            petId=data["petId"],
        )


class Task:
    """Represents a task in the system."""
    
    def __init__(
        self,
        description: str,
        taskType: str,
        priority: int,
        dueDate: date,
        estimatedDuration: int,
        taskId: Optional[str] = None,
        createdAt: Optional[date] = None,
    ):
        """Initialize a new task with the supplied schedule details."""
        self.taskId: str = taskId or str(uuid4())
        self.description: str = description
        self.taskType: str = taskType
        self.priority: int = priority
        self.dueDate: date = dueDate
        self.estimatedDuration: int = estimatedDuration
        self.completed: bool = False
        self.createdAt: date = createdAt or date.today()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the task into a serializable dictionary."""
        return {
            "taskId": self.taskId,
            "description": self.description,
            "taskType": self.taskType,
            "priority": self.priority,
            "dueDate": self.dueDate.isoformat(),
            "estimatedDuration": self.estimatedDuration,
            "completed": self.completed,
            "createdAt": self.createdAt.isoformat(),
        }

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Task":
        """Create a task from a dictionary payload."""
        task = Task(
            description=data["description"],
            taskType=data["taskType"],
            priority=data["priority"],
            dueDate=date.fromisoformat(data["dueDate"]),
            estimatedDuration=data["estimatedDuration"],
            taskId=data.get("taskId"),
            createdAt=date.fromisoformat(data["createdAt"]) if data.get("createdAt") else None,
        )
        task.completed = data.get("completed", False)
        return task


class Weather:
    """Represents weather information."""
    
    def __init__(self, condition: str, temperature: float, recommendation: str):
        """Initialize weather details for a walk schedule."""
        self.condition: str = condition
        self.temperature: float = temperature
        self.recommendation: str = recommendation


class Walk:
    """Represents a scheduled walk."""
    
    def __init__(self, walkId: str, scheduledTime: datetime, durationMinutes: float, weatherCondition: str):
        """Initialize a walk schedule entry."""
        self.walkId: str = walkId
        self.scheduledTime: datetime = scheduledTime
        self.durationMinutes: float = durationMinutes
        self.weatherCondition: str = weatherCondition

    def to_dict(self) -> Dict[str, Any]:
        """Convert the walk into a serializable dictionary."""
        return {
            "walkId": self.walkId,
            "scheduledTime": self.scheduledTime.isoformat(),
            "durationMinutes": self.durationMinutes,
            "weatherCondition": self.weatherCondition,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Walk":
        """Create a walk from a dictionary payload."""
        return Walk(
            walkId=data["walkId"],
            scheduledTime=datetime.fromisoformat(data["scheduledTime"]),
            durationMinutes=data["durationMinutes"],
            weatherCondition=data["weatherCondition"],
        )


class Owner:
    """Represents a pet owner."""
    
    def __init__(
        self,
        name: str,
        email: str,
        preferences: List[str],
        ownerId: Optional[str] = None,
    ):
        """Initialize a pet owner profile."""
        self.ownerId: str = ownerId or str(uuid4())
        self.name: str = name
        self.email: str = email
        self.preferences: List[str] = preferences

    def to_dict(self) -> Dict[str, Any]:
        """Convert the owner into a serializable dictionary."""
        return {
            "ownerId": self.ownerId,
            "name": self.name,
            "email": self.email,
            "preferences": self.preferences,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Owner":
        """Create an owner from a dictionary payload."""
        return Owner(
            name=data["name"],
            email=data["email"],
            preferences=data["preferences"],
            ownerId=data.get("ownerId"),
        )


# ============================================================================
# Manager/Handler Classes
# ============================================================================

class PetManager:
    """Manages pet registration and information."""
    
    def __init__(self):
        """Initialize an empty pet registry."""
        self._registeredPets: Dict[str, Pet] = {}
    
    def addPet(self, name: str, gender: str, weight: float, petType: str) -> Pet:
        """Add a new pet to the registry."""
        if not name:
            raise ValueError("Pet name must not be empty.")
        if weight <= 0:
            raise ValueError("Pet weight must be greater than zero.")
        if not petType:
            raise ValueError("Pet type must not be empty.")

        pet = Pet(name=name, gender=gender, bodyWeight=weight, petType=petType)
        self._registeredPets[pet.petId] = pet
        return pet
    
    def removePet(self, petId: str) -> None:
        """Remove a pet from the registry."""
        try:
            del self._registeredPets[petId]
        except KeyError:
            raise KeyError(f"No pet found with id {petId}")
    
    def getPetInfo(self, petId: str) -> Pet:
        """Get information about a specific pet."""
        try:
            return self._registeredPets[petId]
        except KeyError:
            raise KeyError(f"No pet found with id {petId}")
    
    def listAllPets(self) -> List[Pet]:
        """Get a list of all registered pets."""
        return list(self._registeredPets.values())


class WalkScheduler:
    """Schedules walks for pets considering weather."""
    
    def __init__(self):
        """Initialize an empty walk scheduler."""
        self._currentWeather: Optional[Weather] = None
        self._petSchedules: Dict[str, List[Walk]] = {}
    
    def scheduleWalk(
        self,
        pet: Pet,
        weather: Weather,
        scheduledTime: Optional[datetime] = None,
        durationMinutes: Optional[float] = None,
    ) -> Walk:
        """Schedule a walk for a pet given current weather conditions."""
        if weather is None:
            raise ValueError("Weather information is required to schedule a walk.")

        condition = weather.condition.lower().strip()
        unsafe_conditions = {"storm", "heavy rain", "hurricane", "tornado", "snow", "ice"}
        if condition in unsafe_conditions:
            raise ValueError(f"Cannot schedule a walk in unsafe weather: {weather.condition}")

        if durationMinutes is None:
            durationMinutes = 30.0 if pet.bodyWeight >= 20 else 20.0
        if durationMinutes <= 0:
            raise ValueError("Walk duration must be greater than zero minutes.")

        if scheduledTime is None:
            scheduledTime = datetime.now()

        walk = Walk(
            walkId=str(uuid4()),
            scheduledTime=scheduledTime,
            durationMinutes=durationMinutes,
            weatherCondition=weather.condition,
        )
        self._currentWeather = weather
        self._petSchedules.setdefault(pet.petId, []).append(walk)
        return walk
    
    def setWalkTimestamp(self, walkId: str, dateTime: datetime) -> None:
        """Set or update the timestamp for a scheduled walk."""
        for walk_list in self._petSchedules.values():
            for walk in walk_list:
                if walk.walkId == walkId:
                    walk.scheduledTime = dateTime
                    return
        raise KeyError(f"No walk found with id {walkId}")
    
    def getPetWalkSchedule(self, petId: str) -> List[Walk]:
        """Get the walk schedule for a specific pet."""
        return list(self._petSchedules.get(petId, []))


class TaskManager:
    """Manages tasks and daily task scheduling."""
    
    def __init__(self):
        """Initialize an empty task manager."""
        self._allTasks: Dict[str, Task] = {}
    
    def addTask(self, description: str, task_type: str, priority: int, dueDate: date, estimatedDuration: int = 0) -> Task:
        """Add a new task."""
        if not description:
            raise ValueError("Task description must not be empty.")
        if priority < 0:
            raise ValueError("Task priority must be zero or positive.")
        if dueDate < date.today():
            raise ValueError("Task due date cannot be in the past.")

        task = Task(
            description=description,
            taskType=task_type,
            priority=priority,
            dueDate=dueDate,
            estimatedDuration=estimatedDuration,
        )
        self._allTasks[task.taskId] = task
        return task
    
    def getTodaysTasks(self) -> List[Task]:
        """Get all tasks due today."""
        today = date.today()
        return [
            task
            for task in self._allTasks.values()
            if task.dueDate == today and not task.completed
        ]
    
    def displayTodaysTasks(self) -> None:
        """Display today's tasks in a formatted manner."""
        todays_tasks = self.getTodaysTasks()
        if not todays_tasks:
            print("No tasks due today.")
            return

        print("Today's tasks:")
        for task in sorted(todays_tasks, key=lambda item: item.priority, reverse=True):
            print(
                f"- [{task.taskType}] {task.description} (priority: {task.priority}, "
                f"estimated {task.estimatedDuration} min, id: {task.taskId})"
            )
    
    def completeTask(self, taskId: str) -> None:
        """Mark a task as completed."""
        try:
            task = self._allTasks[taskId]
        except KeyError:
            raise KeyError(f"No task found with id {taskId}")

        if task.completed:
            raise ValueError(f"Task {taskId} is already completed.")
        task.completed = True


class ScheduledActivity:
    """Represents a scheduled activity in the plan."""
    
    def __init__(self, activityId: str, startTime: datetime, endTime: datetime, activityType: str, associatedPet: Pet, associatedTask: Task):
        """Initialize a scheduled activity entry."""
        self.activityId: str = activityId
        self.startTime: datetime = startTime
        self.endTime: datetime = endTime
        self.activityType: str = activityType
        self.associatedPet: Pet = associatedPet
        self.associatedTask: Task = associatedTask

    def to_dict(self) -> Dict[str, Any]:
        """Convert the activity into a serializable dictionary."""
        return {
            "activityId": self.activityId,
            "startTime": self.startTime.isoformat(),
            "endTime": self.endTime.isoformat(),
            "activityType": self.activityType,
            "associatedPetId": self.associatedPet.petId,
            "associatedTaskId": self.associatedTask.taskId,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any], pets_by_id: Dict[str, Pet], tasks_by_id: Dict[str, Task]) -> "ScheduledActivity":
        """Recreate a scheduled activity from stored data."""
        pet = pets_by_id.get(data["associatedPetId"])
        task = tasks_by_id.get(data["associatedTaskId"])
        if pet is None or task is None:
            raise ValueError("Cannot reconstruct ScheduledActivity without matching pet and task data.")
        return ScheduledActivity(
            activityId=data["activityId"],
            startTime=datetime.fromisoformat(data["startTime"]),
            endTime=datetime.fromisoformat(data["endTime"]),
            activityType=data["activityType"],
            associatedPet=pet,
            associatedTask=task,
        )


class ActivityPlan:
    """Represents a complete activity plan for a day."""
    
    def __init__(self, planId: str, planDate: date, activities: List[ScheduledActivity], explanation: str):
        """Initialize an activity plan for a specific date."""
        self.planId: str = planId
        self.planDate: date = planDate
        self.activities: List[ScheduledActivity] = activities
        self.explanation: str = explanation

    def to_dict(self) -> Dict[str, Any]:
        """Convert the plan into a serializable dictionary."""
        return {
            "planId": self.planId,
            "planDate": self.planDate.isoformat(),
            "activities": [activity.to_dict() for activity in self.activities],
            "explanation": self.explanation,
        }

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
        pets_by_id: Dict[str, Pet],
        tasks_by_id: Dict[str, Task],
    ) -> "ActivityPlan":
        """Recreate an activity plan from stored data."""
        activities = [
            ScheduledActivity.from_dict(item, pets_by_id, tasks_by_id)
            for item in data["activities"]
        ]
        return ActivityPlan(
            planId=data["planId"],
            planDate=date.fromisoformat(data["planDate"]),
            activities=activities,
            explanation=data.get("explanation", ""),
        )


class PlanGenerator:
    """Generates optimized activity plans for pet care."""
    
    def __init__(self, pets: Optional[List[Pet]] = None, tasks: Optional[List[Task]] = None):
        """Initialize a plan generator with optional pet and task lists."""
        self._pets: List[Pet] = pets or []
        self._tasks: List[Task] = tasks or []
        self._constraints: Dict[str, str] = {}
        self._priorities: Dict[str, int] = {}
        self._plan: Optional[ActivityPlan] = None
    
    def generatePlan(self, constraints: Dict[str, str], priorities: Dict[str, int]) -> ActivityPlan:
        """Generate an optimized activity plan based on constraints and priorities."""
        if not self._pets:
            raise ValueError("At least one pet is required to generate a plan.")
        if not self._tasks:
            raise ValueError("At least one task is required to generate a plan.")

        self._constraints = constraints or {}
        self._priorities = priorities or {}

        effective_tasks = self._build_effective_task_list()
        activities: List[ScheduledActivity] = []

        start_time = self._parse_start_time(self._constraints.get("earliestStart"))
        max_end = self._parse_end_time(self._constraints.get("latestEnd"))

        if max_end and start_time >= max_end:
            raise ValueError("Constraint latestEnd must be later than earliestStart.")

        current_time = start_time
        pet_index = 0

        for task in effective_tasks:
            activity_duration = max(15, task.estimatedDuration or 30)
            end_time = current_time + timedelta(minutes=activity_duration)

            if max_end and end_time > max_end:
                current_time = self._parse_start_time(self._constraints.get("earliestStart"), shift_days=1)
                end_time = current_time + timedelta(minutes=activity_duration)

            pet = self._pets[pet_index % len(self._pets)]
            activity = ScheduledActivity(
                activityId=str(uuid4()),
                startTime=current_time,
                endTime=end_time,
                activityType=task.taskType,
                associatedPet=pet,
                associatedTask=task,
            )
            activities.append(activity)
            current_time = end_time + timedelta(minutes=10)
            pet_index += 1

        plan_date = date.today()
        explanation = self.explainPlanChoices()
        self._plan = ActivityPlan(
            planId=str(uuid4()),
            planDate=plan_date,
            activities=activities,
            explanation=explanation,
        )
        self.optimizeSchedule()
        return self._plan
    
    def optimizeSchedule(self) -> None:
        """Optimize the current schedule for efficiency."""
        if self._plan is None:
            return

        sorted_activities = sorted(
            self._plan.activities,
            key=lambda activity: (
                activity.associatedTask.priority * -1,
                activity.startTime,
            ),
        )
        self._plan.activities = sorted_activities

    def explainPlanChoices(self) -> str:
        """Generate an explanation of the plan's design choices."""
        constraints_summary = ", ".join(
            f"{key}={value}" for key, value in self._constraints.items()
        ) or "no special constraints"
        priority_override_count = len(self._priorities)
        task_count = len(self._tasks)
        pet_count = len(self._pets)

        return (
            f"Generated a {task_count}-task plan for {pet_count} pet(s) using {constraints_summary}. "
            f"Priority overrides applied to {priority_override_count} task(s)."
        )

    def _build_effective_task_list(self) -> List[Task]:
        """Build and sort the list of tasks that should be scheduled."""
        task_map: Dict[str, Task] = {task.taskId: task for task in self._tasks}
        for task_id, priority in self._priorities.items():
            if task_id in task_map:
                task_map[task_id].priority = priority

        filtered_tasks = [task for task in task_map.values() if not task.completed]
        return sorted(
            filtered_tasks,
            key=lambda task: (task.dueDate, -task.priority, task.description),
        )

    def _parse_start_time(self, time_string: Optional[str], shift_days: int = 0) -> datetime:
        """Parse a start time constraint into a datetime."""
        if time_string:
            try:
                hours, minutes = map(int, time_string.split(":"))
                return datetime.combine(date.today() + timedelta(days=shift_days), time(hour=hours, minute=minutes))
            except Exception:
                raise ValueError("Invalid earliestStart constraint format. Use HH:MM.")

        return datetime.combine(date.today() + timedelta(days=shift_days), time(hour=9, minute=0))

    def _parse_end_time(self, time_string: Optional[str]) -> Optional[datetime]:
        """Parse an end time constraint into a datetime."""
        if time_string:
            try:
                hours, minutes = map(int, time_string.split(".")) if "." in time_string else map(int, time_string.split(":"))
                return datetime.combine(date.today(), time(hour=hours, minute=minutes))
            except Exception:
                raise ValueError("Invalid latestEnd constraint format. Use HH:MM.")
        return None


class PersistenceManager:
    """Handles serialization of pawpal data to persistent JSON files."""

    @staticmethod
    def save_state(
        file_path: str,
        pets: List[Pet],
        tasks: List[Task],
        walks: List[Walk],
        owners: Optional[List[Owner]] = None,
        plans: Optional[List[ActivityPlan]] = None,
    ) -> None:
        """Persist the current application state to a JSON file."""
        owners = owners or []
        plans = plans or []
        state = {
            "pets": [pet.to_dict() for pet in pets],
            "tasks": [task.to_dict() for task in tasks],
            "walks": [walk.to_dict() for walk in walks],
            "owners": [owner.to_dict() for owner in owners],
            "plans": [plan.to_dict() for plan in plans],
        }
        with open(file_path, "w", encoding="utf-8") as handle:
            json.dump(state, handle, indent=2)

    @staticmethod
    def load_state(file_path: str, load_plans: bool = False) -> Dict[str, Any]:
        """Load persisted application state from a JSON file."""
        with open(file_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)

        pets = [Pet.from_dict(item) for item in data.get("pets", [])]
        tasks = [Task.from_dict(item) for item in data.get("tasks", [])]
        walks = [Walk.from_dict(item) for item in data.get("walks", [])]
        owners = [Owner.from_dict(item) for item in data.get("owners", [])]

        plans = []
        if load_plans:
            pet_map = {pet.petId: pet for pet in pets}
            task_map = {task.taskId: task for task in tasks}
            plans = [
                ActivityPlan.from_dict(item, pet_map, task_map)
                for item in data.get("plans", [])
            ]

        return {
            "pets": pets,
            "tasks": tasks,
            "walks": walks,
            "owners": owners,
            "plans": plans,
        }
