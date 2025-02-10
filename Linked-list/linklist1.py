# Linked List with Basic Numerical Data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

    # Method to add a node to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node 

    # Method to print all elements of the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating the linked list
linked_list = LinkedList()

# Appending elements
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Linked List with numerical data:")
linked_list.print_list()  
