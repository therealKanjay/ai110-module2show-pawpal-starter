# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. The assistant should:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints such as available time and task priority
- Produce a daily plan and explain the reasoning behind it

The current implementation focuses on the core logic in Python and persistence support. The Streamlit UI is still the next integration step.

## What is implemented

- `pawpal_system.py` contains:
  - `Pet`, `Task`, `Walk`, `Owner`, `ScheduledActivity`, `ActivityPlan`
  - `PetManager`, `TaskManager`, `WalkScheduler`, `PlanGenerator`, and `PersistenceManager`
- `TaskManager` supports task creation, completion, and today-only task listing
- `WalkScheduler` supports weather-based scheduling and per-pet walk plans
- `PlanGenerator` builds a daily activity plan using constraints, priorities, and available pets
- `PersistenceManager` saves and loads app state as JSON
- `test_pawpal_system.py` includes core behavior validation

## Getting started

### Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Run tests

```bash
python -m pytest -q
```

### Sample output

Running the demo script prints a simple daily schedule like this:

```text
Today's Schedule
Owner: Alex
- 08:00 | Milo | Feed Milo breakfast
- 12:30 | Buddy | Take Buddy for a walk
- 19:00 | Milo | Play with Milo
```

## Usage notes

- Use `PetManager.addPet()` and `TaskManager.addTask()` to create pets and tasks
- Use `WalkScheduler.scheduleWalk()` to schedule a pet walk with weather validation
- Use `PlanGenerator.generatePlan()` to build a daily plan for one or more pets
- Use `PersistenceManager.save_state()` and `load_state()` to persist pets, tasks, walks, owners, and plans

## 🧪 Current test coverage

The test file covers:

- persistence save/load behavior
- weather validation in walk scheduling
- plan generation for multiple tasks

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `PlanGenerator._build_effective_task_list()` | orders by due date, priority, description |
| Constraint handling | `PlanGenerator.generatePlan()` | supports `earliestStart` and `latestEnd` |
| Weather validation | `WalkScheduler.scheduleWalk()` | rejects unsafe weather conditions |
| Persistence | `PersistenceManager` | saves pets, tasks, walks, owners, plans to JSON |

## 📸 Demo Walkthrough

1. Add a pet using `PetManager.addPet()`.
2. Create tasks using `TaskManager.addTask()`.
3. Schedule walks with `WalkScheduler.scheduleWalk()`.
4. Build a daily plan with `PlanGenerator.generatePlan()`.
5. Save or restore state using `PersistenceManager.save_state()` and `load_state()`.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
