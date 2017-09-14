# The program is related to while loop statement
# Allow the user to enter a sequence of non-negative
# numbers. The user ends the list with a negative
# numbers. At the end the sum of the non-negative
# numbers entered is displayed. The program prints
# zero if the user provides no non-negative numbers

entry = 0  # Ensure the loop is entered
sum = 0    # Initialize sum

# Request input from the user
print("Enter numbers to sum, negative number ends list:")

while entry >= 0:             # A negative number exits the loop
    entry = eval(raw_input())     # Get the value
    if entry >= 0:            # Is number non-negative
        sum += entry          # Only add it if it is non-negative
print("sum =", sum)           # Display the sum