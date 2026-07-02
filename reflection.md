# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
    My initial design has 4 classes, first one adds a pet that basically does what it says.
    It looks up already registered pets so it doesn't accidently duplicates, and then
    asks for general & specific questions about the pet.
    Schedule a walk lets you schedule a walk with any pet of your choosing.
    It adds a timestamp to your schedule where it decided that on that time is the best to walk your pet
    See today's tasks lets you see the tasks that are due today
    Generating a plan based on constraints & priorities allows you to create 
    a whole new plan that is based on the constraints & preferences that you've laid out
- What classes did you include, and what responsibilities did you assign to each?
    -Add a pet
        Attributes: already registered pets, every recorded animal information
        Methods: Add a pet with their name, gender, body weight, type of pet (has to be specific, not just "Dog" or "Cat")
    -Schedule a walk
        Attributes: Pet information, weather information
        Methods: Set a timestamp on when it is best to take your pet out for a walk
    -See today's tasks
        Attributes: tasks that are due today
        Method: display the current tasks today
    -Generate a plan based on constraints & priorities
        Attributes: pet information, all tasks, any constraints & priorities
        Method: create a plan based on constraints & priorities

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
