# Chapter -7 Using Functions

# Print a massage to prompt the user for input
# Adds together two integers
def prompt(n):
    value = int(input("Please enter integer #") )
    return value
print("This program adds together two integers.")
value1 = prompt(1)          # Call the function
value2 = prompt(2)          # Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)           # Report results