# basics of functions
# print a message to prompt the user for input
from __future__ import print_function
def prompt():
    print("Please enter an integer value: ", end="")
# start of program
print("This program adds together two integers.")
prompt()   # call the function
value = int(raw_input())
prompt()    # call the function again
value2 = int(raw_input())
sum = value + value2;
print(value,"+", value2, "=", sum )