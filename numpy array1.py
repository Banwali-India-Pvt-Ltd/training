print ("my question = Write a Python program to convert a list and tuple into arrays")
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(my_tuple))

print ("my question = Write a Python program to append values to the end of an array.")
import numpy as np
x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x, [[40, 50, 60], [70, 80, 90]])
print("After append values to the end of the array:")
print (x)
import numpy as np
# Create an empty array
x = np.empty((1,1))
print(x)
# Create a full array
y = np.full((3,3),6)
print(y)

print ("my question = Write a Python program to convert the values of Centigrade degrees into Fahrenheit degrees.")
import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:")
print(5*F/9 - 5*32/9)

import numpy as np
print ("my question = Write a Python program to find the real and imaginary parts of an array of complex numbers.")
import numpy as np
x = np.sqrt([1+0j, 0+1j])
print("Original array",x)
print("Real part of the array:")
print(x.real)
print("Imaginary part of the array:")
print(x.imag)

print ("my question =  Write a Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.")
import numpy as np
x = np.array([1,2,3], dtype=np.float64)
import numpy as np
x = np.array([1,2,3], dtype=np.float64)
print("Size of the array: ", x.size)
print("Length of one array element in bytes: ", x.itemsize)
print("Total bytes consumed by the elements of the array: ", x.nbytes)


print ("my question =  Write a Python program to test whether each element of a 1-D array is also present in a second array.")
import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))

print ("my question = Write a Python program to find common values between two arrays")
import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))

print ("my question = Write a Python program to get the unique elements of an array")
import numpy as np
x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
x = np.array([[1, 1], [2, 3]])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))

print ("my question = Write a Python program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2")
import numpy as np
array1 = np.array([0,10,20,40,60,80])
array2 = [10,30,40,50,70]
print (np.setdiff1d(array1, array2))
















