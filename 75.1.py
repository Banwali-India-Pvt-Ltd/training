# The program provides a conditional expression's

# Acquire a number from the user and print its absolute value

from __future__ import print_function
n = eval(raw_input("Enter a number:"))
print('|', n, '| =', (-n if n < 0 else n), sep='')