# Chapter -7 Using Functions

# Print a massage to prompt the user for input
# Adds together two integers.
def prompt():
    value = int(input("Please enter an integer value: "))
    return value
print("This program adds together two integers.")
value1 = prompt()        # Call the function
value2 = prompt()        # Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)           # Report Results
