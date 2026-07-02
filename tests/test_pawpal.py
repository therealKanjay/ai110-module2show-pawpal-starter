from datetime import date

from pawpal_system import Pet, Task


def test_task_mark_complete_updates_status():
    task = Task(
        description="Feed the pet",
        taskType="Feeding",
        priority=1,
        dueDate=date.today(),
        estimatedDuration=10,
    )

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_adding_task_to_pet_increases_task_count():
    pet = Pet(name="Buddy", gender="Male", bodyWeight=12.0, petType="Dog")
    task = Task(
        description="Walk Buddy",
        taskType="Exercise",
        priority=2,
        dueDate=date.today(),
        estimatedDuration=20,
    )

    assert pet.task_count == 0

    pet.add_task(task)

    assert pet.task_count == 1
    assert pet.tasks[0] is task
