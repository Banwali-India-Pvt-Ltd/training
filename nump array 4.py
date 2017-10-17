import numpy as np
a = np.array([[6,7,8],[1,2,3],[9,3,2]])
print a
for row in a :
    print row
for cell in a.flat:
    print cell
a =np.arange(6).reshape(3,2)
b =np.arange(6,12).reshape(3,2)
print a
print b
print np.vstack((a,b))
print np.hstack((a,b))
a =np.arange(30).reshape(2,15)
print a
print np.hsplit(a,3)
print np.vsplit(a,2)
a =np.arange(12).reshape(3,4)
print a
b = a > 4
print b
print a[b]
print a[b] -1
print a

print ("31. Write a Python program to get the values and indices of the elements that are bigger than 10 in a given array.")
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))

print ("32. Write a Python program to save a NumPy array to a text file.")
import numpy as np
a = np.arange(1.0, 2.0, 36.2)
np.savetxt('file.out', a, delimiter=',')

print ("33. Write a Python program to find the memory size of a NumPy array.")
import numpy as np
n = np.zeros((4,4))
print("%d bytes" % (n.size * n.itemsize))

print ("34. Write a Python program to create an array of ones and an array of zeros.")
import numpy as np
print("Create an array of zeros")
x = np.zeros((1,2))
print("Default type is float")
print(x)
print("Type changes to int")
x = np.zeros((1,2), dtype = np.int)
print(x)
print("Create an array of ones")
y= np.ones((1,2))
print("Default type is float")
print(y)
print("Type changes to int")
y = np.ones((1,2), dtype = np.int)
print(y)

print ("35. Write a Python program to change the dimension of an array.")
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("6 rows and 0 columns")
print(x.shape)

y = np.array([[1, 2, 3],[4, 5, 6],[7,8,9]])
print("(3, 3) -> 3 rows and 3 columns ")
print(y)

x = np.array([1,2,3,4,5,6,7,8,9])
print("Change array shape to (3, 3) -> 3 rows and 3 columns ")
x.shape = (3, 3)
print(x)