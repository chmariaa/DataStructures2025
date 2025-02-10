# Stack Used for Undo Operation
action_stack = []

current_text = "Hello"
print("\nInitial text:", current_text)

action_stack.append(current_text)
current_text += " World"
print("\nAfter typing:", current_text)

action_stack.append(current_text) 
current_text += "!"
print("After typing more:", current_text)

previous_text = action_stack[-1]  
print("After undoing the last action:", previous_text)

current_text = previous_text
