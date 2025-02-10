# Array Used for Storing Names
employees = ["Alice", "Bob", "Charlie", "David", "Eva"]

print("\nEmployee names:", employees)

print("\nEmployee at index 1:", employees[1]) 
print("Employee at index 4:", employees[4])  

# Adding a new employee name to the array (list)
employees.append("Frank") 
print("\nEmployee names after adding Frank:", employees)

# Removing an employee name from the array
employees.remove("Charlie")
print("Employee names after removing Charlie:", employees)

print("\nEmployee names in the company:")
for employee in employees:
    print(employee)
