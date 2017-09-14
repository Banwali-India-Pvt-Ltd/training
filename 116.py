def add(a ,b = 0):
    return a+b
print (add(1))



def foo(i, a = ['kuldeep']):
    a.append(i)
    return a
print(foo(1))
print(foo(2))
