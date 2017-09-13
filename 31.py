# The program allows us to control how the print function
# seprates the arguments it displays

# print uses a keyword argument named to specify the string to use
# insert between items
from __future__ import  print_function
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)   # it will print numbers with a space
print(w, x, y, z, sep=',')  # it will print numbers with a seprated comma
print(w, x, y, z, sep='')   # it will print numbers with a blank space
print(w, x, y, z, sep=':') # it will print numbers with : into them
print(w, x, y, z, sep='-----') # it will print numbers with ----- into them