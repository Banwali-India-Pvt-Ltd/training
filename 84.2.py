from __future__ import  print_function
n = eval(input("Enter a number:"))
print('|', n, '| = ', (-n if n < 0 else n), sep='')
