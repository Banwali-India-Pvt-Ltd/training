from __future__ import print_function
#  Acquire a number from the user and print and print its absolute value
n = eval(input("Enter a number: "))
print('|', n, '| =', (-n if n < 0 else n), sep='')