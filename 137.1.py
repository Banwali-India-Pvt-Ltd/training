# Definition of the prompt function
def prompt():
    value = int(raw_input("Please enter an integer value:"))
    return value

print("This program adds together two integers.")
value = prompt()  # Call the function
value2 = prompt()  # call the function again

sum = value + value2
print(value, "+", value2, "=", sum)