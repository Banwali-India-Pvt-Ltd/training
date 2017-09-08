#Exception handing in python
(x,y) = (1,4)
try:
    z = x/y
    print ('division successful')
    #some other code.
except ZeroDivisionError:
    print('divide by zero')
