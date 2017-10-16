import numpy as np
print ("my question = Write a Python program to find the union of two arrays. Union will return the unique, sorted array of values that are in either of the two input arrays.")
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique sorted array of values that are in either of the two input arrays:")
print(np.union1d(array1, array2))

print ("my question = Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays.")
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(array1, array2))

print ("my question =  Write a Python program to test if all elements in an array evaluate to True")
import numpy as np
print(np.all([[True,False],[True,True]]))
print(np.all([[True,True],[True,True]]))
print(np.all([10, 20, 0, -50]))
print(np.all([10, 20, -50]))

print ("my question = Write a Python program to test whether any array element along a given axis evaluates to True.")
import numpy as np
print (np.any([[False,False],[False,False]]))
print (np.any([[True,True],[True,True]]))
print (np.any([10, 20, 0, -50]))
print (np.any([10, 20, -50]))

print ("my question =  Write a Python program to construct an array by repeating. ")
import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)
print("Repeating 2 times")
x = np.tile(a, 2)
print(x)
print("Repeating 3 times")
x = np.tile(a, 3)
print(x)

print ("my question = Write a Python program to repeat elements of an array.")
import numpy as np
x  = np.repeat(3,4)
print x
x = np.array([[1,2],[3,4]])
print (np.repeat(x, 2))

print ("my question = Write a Python program to find the indices of the maximum and minimum values along the given axis of an array.")
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print ("original", x)
print ("Maximum value",np.argmax(x))
print ("Minimum value",np.argmin(x))

print ("my question = Write a Python program compare two arrays using numpy.")
import numpy as np
a = np.array([1, 2])
b = np.array([4, 5])
print ("array a",a)
print ("array b",b)
print ("a > b")
print (np.greater(a,b))
print ("a >= b")
print (np.greater_equal(a, b))
print ("a < b")
print (np.less(a, b))
print ("a <= b")
print (np.less_equal(a, b))

print ("my question = Write a Python program to sort an along the first, last axis of an array.")
import numpy as np
a = np.array([[4, 6],[2, 1]])
print ("Original array:", a)
x = np.sort(a,axis=0)
print x
y = np.sort(x,axis=1)
print y

print ("my question = Write a Python program to sort an along the first, last axis of an array.")
import numpy as np
first_names = ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
last_name = ('Woolum', 'Battle', 'Plitner', 'Brien', 'Stah1')
x = np.sort((first_names, last_name))
print x