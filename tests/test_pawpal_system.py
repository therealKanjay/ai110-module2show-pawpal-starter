import json
from datetime import date, datetime
from pawpal_system import (
    ActivityPlan,
    Owner,
    Pet,
    PersistenceManager,
    PlanGenerator,
    TaskManager,
    Walk,
    WalkScheduler,
    Weather,
)


def test_pet_and_task_persistence(tmp_path):
    pet = Pet(name="Fido", gender="Male", bodyWeight=10.0, petType="Dog")
    task_manager = TaskManager()
    task = task_manager.addTask(
        description="Feed Fido",
        task_type="Feeding",
        priority=2,
        dueDate=date.today(),
        estimatedDuration=15,
    )
    weather = Weather(condition="Clear", temperature=72.0, recommendation="Sunny walk")
    walk = Walk(walkId="walk-1", scheduledTime=datetime.now(), durationMinutes=20, weatherCondition=weather.condition)
    owner = Owner(name="Alice", email="alice@example.com", preferences=["morning"])
    plan = ActivityPlan(planId="plan-1", planDate=date.today(), activities=[], explanation="Test plan")

    file_path = tmp_path / "state.json"
    PersistenceManager.save_state(
        str(file_path),
        pets=[pet],
        tasks=[task],
        walks=[walk],
        owners=[owner],
        plans=[plan],
    )

    loaded = PersistenceManager.load_state(str(file_path), load_plans=True)
    assert len(loaded["pets"]) == 1
    assert len(loaded["tasks"]) == 1
    assert len(loaded["walks"]) == 1
    assert len(loaded["owners"]) == 1
    assert isinstance(loaded["pets"][0], Pet)
    assert loaded["tasks"][0].description == "Feed Fido"


def test_walk_scheduler_weather_validation():
    pet = Pet(name="Buddy", gender="Male", bodyWeight=25.0, petType="Dog")
    scheduler = WalkScheduler()
    bad_weather = Weather(condition="Storm", temperature=55.0, recommendation="Stay indoors")
    try:
        scheduler.scheduleWalk(pet=pet, weather=bad_weather)
        raise AssertionError("Expected ValueError for unsafe weather")
    except ValueError:
        pass


def test_plan_generator_schedules_tasks():
    pets = [Pet(name="Milo", gender="Male", bodyWeight=8.0, petType="Cat")]
    task_manager = TaskManager()
    task_manager.addTask(
        description="Clean litter box",
        task_type="Cleaning",
        priority=1,
        dueDate=date.today(),
        estimatedDuration=10,
    )
    task_manager.addTask(
        description="Play time",
        task_type="Exercise",
        priority=3,
        dueDate=date.today(),
        estimatedDuration=20,
    )
    generator = PlanGenerator(pets=pets, tasks=list(task_manager._allTasks.values()))
    plan = generator.generatePlan(constraints={"earliestStart": "08:00"}, priorities={})
    assert plan.planDate == date.today()
    assert len(plan.activities) == 2
    assert plan.explanation.startswith("Generated a 2-task plan")
