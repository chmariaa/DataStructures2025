# Queue Used in a Task Scheduling System
task_queue = []

task_queue.append("Task 1: Prepare report")
task_queue.append("Task 2: Email updates")   
task_queue.append("Task 3: Clean office")   
print("\nTask queue after tasks arrive:", task_queue)

# Dequeue: Processing the first task in the queue
completed_task = task_queue.pop(0)  
print("\nCompleted task:", completed_task)
print("Task queue after completing one task:", task_queue)

# Another dequeue: Processing the next task
completed_task = task_queue.pop(0)
print("\nCompleted task:", completed_task)
print("Task queue after completing another task:", task_queue)
