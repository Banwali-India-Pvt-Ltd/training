from __future__ import  print_function
 #a and b are distinct lists that contain the same elemant
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print ('Is ', a, 'equal to ', b, '?', sep=' ', end=' ')
print (a == b)
print ('Are ', a, ' and ', b, 'aliases?', sep=' ', end=' ')
#c and alias are distinct listinct lists that contain the same elements
c = [100, 200, 300, 400]
d = c    # Makes d an alias of c
print ('Is ', c, 'equal to ', d, '?', sep=' ', end=' ')
print (c == d)
print ('Are ', c, 'and ', d, 'aliases?', sep=' ', end=' ')
print (c is d)
