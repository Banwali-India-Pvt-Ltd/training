import numpy as np
array1 = np.array([2,3,4,5,6])
array2 = np.array([6,5,4,3,2])
print array1
print array2
print (array1 * array2)


array_A = np.array([1,2,3,4])
print array_A
print (array_A * 2)
print (array_A * array_A)
print (array_A + array_A)


import numpy as np
a = np.array([5,6,9])
print a[0]
print a[1]


a = np.array([[[[1,2], [3,4], [5,6]]]])
print a.ndim
print a.itemsize

a = np.array([[5,6,7,8],[1,2,3,4]])
print a.ndim
print a.itemsize
print a.dtype

a = np.array([[1,2],[3,4],[5,6]], dtype=float)
print a.itemsize
print a.dtype
print a

print a.size
print a.shape

a=np.array([[1,2],[3,4],[5,6]], dtype=complex)
print a

a=np.zeros((3,4))
print a

a=np.ones((3,4))
print a

print np.arange(1,5)
print np.arange(1,5,2)

print np.linspace(1,5,10)

import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print a.shape
print a.reshape(2,3)
print a.reshape(6,1)
print a.ravel()
print a.min()
print a.max()
print a.sum()
print a.sum(axis=0)
print a.sum(axis=1)

a=np.array([[1,2],[3,4],[5,6]])
print np.sqrt(a)
print np.std(a)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print a+b
print a/b
print a-b
print a*b
print a%b
print a.dot(b)