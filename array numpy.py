
print ("your question =  Write a Python program to print the NumPy version in your system.")
import numpy as np
print (np.__version__)

print ("your question =  Write a Python program to count the number of characters (character frequency) in a string.")
import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional numpy array: ",a)

print ("your question = Create a 3x3 matrix with values ranging from 2 to 10")
import numpy as np
x =  np.arange(2, 11).reshape(3,3)
print(x)

print ("your question = Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself")
import numpy as np
x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)

print ("your question =  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string")
import numpy as np
x = np.arange(12, 38)
print(x)

print ("your question =  Write a Python program to reverse an array (first element becomes last)")
import numpy as np
x = np.arange(12,38)
print x[::-1]


print ("your question =  Write a Python program to an array converted to a float type.")
import numpy as np
a = [1,2,3,4]
x = np.asfarray(a)
print x

#Write a Python program to create a 2d array with 1 on the border and 0 inside
print ("your question = Write a Python program to create a 2d array with 1 on the border and 2 inside")
import numpy as np
x = np.ones((5,5))
x[1:-1,1:-1] = 2
print x

print ("your question = Write a Python program to remove the nth index character from a nonempty string")
import numpy as np
x = np.ones((3,3))
print x
x = np.pad(x, pad_width=1,mode='constant', constant_values=0)
print x

print ("your question = Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern")
import numpy as np
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print x

















