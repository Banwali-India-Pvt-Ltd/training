# definition of the prompt function
# getting error in this program
from __future__ import print_function
def prompt(n):
    value = int(raw_input("Please enter integer #", n, ": ", sep=""))
    return value

print("This program adds together two integerss.")
value1 = prompt(1) # call the function
value2 = prompt(2)  # call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)
