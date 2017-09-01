from math import *
print (eval('dir()',{'squarRoot': sqrt, 'pow': pow}))
print (eval('squareRoot(9)', {'squareRoot': sqrt, 'pow': pow}))