# Linked List Used for Storing Employee Names
class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.next = None 

class EmployeeLinkedList:
    def __init__(self):
        self.head = None  

    # Method to add an employee to the linked list
    def add_employee(self, name):
        new_employee = EmployeeNode(name)
        if not self.head:
            self.head = new_employee  
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_employee 

    # Method to print all employee names in the list
    def print_employees(self):
        current = self.head
        while current:
            print(current.name, end=" -> ")
            current = current.next
        print("None")

# Creating the employee linked list
employee_list = EmployeeLinkedList()

# Adding employees to the list
employee_list.add_employee("Alice")
employee_list.add_employee("Bob")
employee_list.add_employee("Charlie")

print("Employee Linked List:")
employee_list.print_employees() 
