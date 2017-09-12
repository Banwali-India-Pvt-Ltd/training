#python reduce
from functools import reduce
#reduce (binary-funstion,sequence)
p = reduce(lambda x,y: x*y,[1, 2, 3, 4])
print (p)






from functools import reduce
def f(x, y):
    return x*y
p = reduce(f,[1, 2, 3, 4])
print (p)