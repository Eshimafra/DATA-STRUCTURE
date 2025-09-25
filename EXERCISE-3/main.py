# DATA STRUCTURE - BIT - EXERCISE NO:4
# Project 20

# ------------------- Stack Questions -------------------

print("STACK PRACTICAL 1 (MoMo App):")
stack = ["Dial Code", "Enter PIN", "Select Service"]
print("Initial stack:", stack)
undone_step = stack.pop()
print("After pop:", stack)
print("Undone step:", undone_step)
print("\n--- Screenshot-style Output ---")
print("Initial stack: ['Dial Code', 'Enter PIN', 'Select Service']")
print("After pop: ['Dial Code', 'Enter PIN']")
print("Undone step: Select Service")
print("\n")

print("STACK PRACTICAL 2 (UR Student):")
stack = ["Revise Notes", "Group Work", "Mock Exam"]
print("Initial stack:", stack)
stack.pop()
stack.pop()
print("After popping two:", stack)
top_step = stack[-1]
print("Top of stack:", top_step)
print("\n--- Screenshot-style Output ---")
print("Initial stack: ['Revise Notes', 'Group Work', 'Mock Exam']")
print("After popping two: ['Revise Notes']")
print("Top of stack: Revise Notes")
print("\n")

# ------------------- Stack Challenge -------------------
print("STACK CHALLENGE TRACE:")
# 1. Start with empty stack
stack = []
# 2. Push Task1, Task2, Task3, Task4
stack.append("Task1")   # stack: ['Task1']
stack.append("Task2")   # stack: ['Task1', 'Task2']
stack.append("Task3")   # stack: ['Task1', 'Task2', 'Task3']
stack.append("Task4")   # stack: ['Task1', 'Task2', 'Task3', 'Task4']
print("After pushes:", stack)
# 3. Pop twice
stack.pop()             # removes 'Task4'
stack.pop()             # removes 'Task3'
print("After 2 pops:", stack)
# 4. Push new task
stack.append("Task5")   # stack: ['Task1', 'Task2', 'Task5']
print("After pushing Task5:", stack)
print("\nAlgorithmic Steps:")
print("1. Start with empty stack")
print("2. Push Task1, Task2, Task3, Task4")
print("3. Pop twice (removes Task4, Task3)")
print("4. Push Task5")
print("Final stack:", stack)
print("\n")

# ------------------- Stack Reflection -------------------
print("STACK REFLECTION:")
print("Stack fits undo better than redo because undo requires reversing the most recent actions (LIFO), while redo needs to remember undone actions in order (which is not LIFO).")

# ------------------- Queue Questions -------------------

print("\nQUEUE PRACTICAL 1 (CHUK):")
queue = ["Patient1", "Patient2", "Patient3", "Patient4", "Patient5"]
print("Initial queue:", queue)
queue.pop(0)  # Serve first patient
print("After serving one:", queue)
print("Patient in front:", queue[0])
print("\n--- Screenshot-style Output ---")
print("Initial queue: ['Patient1', 'Patient2', 'Patient3', 'Patient4', 'Patient5']")
print("After serving one: ['Patient2', 'Patient3', 'Patient4', 'Patient5']")
print("Patient in front: Patient2")
print("\n")

print("QUEUE PRACTICAL 2 (Airtel):")
queue = ["Client1", "Client2", "Client3"]
print("Initial queue:", queue)
print("Client served last:", queue[-1])
print("\n--- Screenshot-style Output ---")
print("Initial queue: ['Client1', 'Client2', 'Client3']")
print("Client served last: Client3")
print("\n")

# ------------------- Queue Challenge -------------------
print("QUEUE CHALLENGE (Kigali Arena):")
print("Algorithmic Steps:")
print("1. Initialize empty queue.")
print("2. As each person arrives, enqueue them at the end.")
print("3. When entry opens, dequeue from the front one by one.")
print("4. This ensures first-come, first-served order.")
print("Stack is not suitable because it would serve the last person who arrived first, which is unfair.")

# ------------------- Queue Reflection -------------------
print("\nQUEUE REFLECTION:")
print("FIFO ensures orderliness in mass events by serving people in the order they arrived, preventing disputes and maintaining fairness.")