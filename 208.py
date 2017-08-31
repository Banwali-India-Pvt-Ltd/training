#file name is prefixsuffix
from __future__ import  print_function
a = [1, 2, 3, 4, 5, 6, 7, 8]
print ("prefixes of", a)
for i in range(0,len(a)+ 1):
    print ('<', a[0:i], '>', sep='')
print('----------------------------------')
print('Suffixes of', a)
for i in range(0, len (a) + 1):
    print ('<',a[i:len (a)+ 1], '>')