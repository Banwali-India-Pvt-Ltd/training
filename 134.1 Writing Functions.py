# Chapter -7 Writing Functions

# Print a massage to prompt the user for input
# Adds together two integers.

from __future__ import print_function
def prompt():
    print("Please enter an integer value: ", end="  ")
print("This program adds together two integers.")     # Start of program
prompt()       # Call the function
value1 = int(input())
prompt()       # Call the function again
value2 = int(input())
sum = value1 + value2;          # Add t
print(value1, "+", value2, "=", sum)              # Report results