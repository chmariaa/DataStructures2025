# Queue with Enqueue and Dequeue Operations
queue = []

queue.append(101)  
queue.append(102)  
queue.append(103) 

print("\nQueue after people arrive:", queue)

# Dequeue: Serving the first person in the queue
served_person = queue.pop(0) 
print("\nServed person:", served_person)
print("Queue after serving one person:", queue)

# Another dequeue: Serving the next person
served_person = queue.pop(0)
print("\nServed person:", served_person)
print("Queue after serving another person:", queue)
