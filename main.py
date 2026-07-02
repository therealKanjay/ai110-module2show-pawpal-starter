from datetime import date, datetime, time, timedelta

from pawpal_system import Owner, Pet, ScheduledActivity, TaskManager


def main() -> None:
    owner = Owner(
        name="Alex",
        email="alex@example.com",
        preferences=["morning walks", "playtime"],
    )

    pets = [
        Pet(name="Milo", gender="Male", bodyWeight=8.0, petType="Cat"),
        Pet(name="Buddy", gender="Male", bodyWeight=25.0, petType="Dog"),
    ]

    task_manager = TaskManager()
    today = date.today()

    schedule_times = [
        (time(8, 0), pets[0], "Feed Milo breakfast"),
        (time(12, 30), pets[1], "Take Buddy for a walk"),
        (time(19, 0), pets[0], "Play with Milo"),
    ]

    activities = []
    for scheduled_time, pet, description in schedule_times:
        task = task_manager.addTask(
            description=description,
            task_type="Care",
            priority=1,
            dueDate=today,
            estimatedDuration=30,
        )
        start_time = datetime.combine(today, scheduled_time)
        end_time = start_time + timedelta(minutes=30)
        activities.append(
            ScheduledActivity(
                activityId=f"activity-{len(activities) + 1}",
                startTime=start_time,
                endTime=end_time,
                activityType="Care",
                associatedPet=pet,
                associatedTask=task,
            )
        )

    print("Today's Schedule")
    print(f"Owner: {owner.name}")
    for activity in activities:
        print(
            f"- {activity.startTime.strftime('%H:%M')} | {activity.associatedPet.name} | {activity.associatedTask.description}"
        )


if __name__ == "__main__":
    main()
