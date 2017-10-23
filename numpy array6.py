print ("my question no. 36= Write a Python program to create a contiguous flattened array")
import numpy as np
x = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array:")
print(x)
y = np.ravel(x)
print("New flattened array:")
print(y)
print("\n")
print ("my question no. 37=  Write a Python program to create a 2-dimensional array of size 2 x 3 (composed of 4-byte integer elements), also print the shape, type and data type of the array.")
import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(type(x))
print(x.shape)
print(x.dtype)
print ("my question no. 38= . Write a Python program to count occurrences of a substring in a string.")
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
y = np.reshape(x,(3,2))
print("Reshape 3x2:")
print(y)
z = np.reshape(x,(2,3))
print("Reshape 2x3:")
print(z)
print ("my question no. 39=  Write a Python program to change the data type of an array.")
import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)
print("Data type of the array x is:",x.dtype)
# Change the data type of x
y = x.astype(float)
print("New Type: ",y.dtype)
print(y)
print ("my question no. 40=  Write a Python program to reverse words in a string")
import numpy as np
#using no.full
x = np.full((3, 5), 2, dtype=np.uint)
print(x)
#using no.ones
y = np.ones([3, 5], dtype=np.uint) *2
print(y)
print ("my question no. 41=  Write a Python program to create an array of 10's with the same shape and type of an given array.")
import numpy as np
x = np.arange(4, dtype=np.int64)
y = np.full_like(x, 10)
print(y)
print ("my question no. 42= Write a Python program to create a 3-D array with ones on the diagonal and zeros elsewhere")
import numpy as np
x = np.eye(3)
print(x)
print ("my question no. 43 =  Write a Python program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere.")
import numpy as np
x = np.diagflat([4,5,6,8])
print (x)
print ("my question no. 44=  Write a Python program to create a 1-D array going from 0 to 50 and an array from 10 to 50.")
import numpy as np
x = np.arange(50)
print("Array from 0 to 50:")
print(x)
x = np.arange(10, 50)
print("Array from 10 to 50:")
print(x)
print ("my question no. 45= Write a Python program to Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive.")
import numpy as np
x = np.linspace(2.5, 6.5, 30)
print(x)
print ("my question no. 46= Write a Python program to to create a 1-D array of 20 element spaced evenly on a log scale between 2. and 5., exclusive. ")
import numpy as np
x =  np.logspace(2., 5., 20, endpoint=False)
print(x)
print("my question no. 47= Write a Python program to create an array which looks like below array.")
import numpy as np
x = np.tri(4, 3, -1)
print(x)
print ("my question no.48= Write a Python program to create an array which looks like below array.")
import numpy as np
x = np.triu(np.arange(2, 14).reshape(4, 3), -1)
print(x)
print ("my question no. 49 = Write a Python program to collapse a 3-D array into one dimension array.")
import  numpy as np
x = np.eye(3)
print ("3-D array:")
print (x)
f = np.ravel(x, order= 'F')
print (f)
print ("my question no 50 = . Write a Python program to find the 4th element of a specified array. ")
import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)
e1 = x.flat[3]
print("Forth e1ement of the array:")
print(e1)