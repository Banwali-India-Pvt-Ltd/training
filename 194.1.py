# Chapter 9 ( List )
# 9.2 List Assignment and equivalence

# When comparing lists lst1 and lst2, if the expression list1 is lst2 evaluates to True,
# the expression lst1 == lst2 is guaranteed to be True.
# a and b are distinct lists that contain the same elemetns
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print('Is ', a, ' equal to ', b, '?')
print(a == b)

print('Are ', a, ' and', b, ' aliases?')
print(a is b)

# c and d alias are distinct lists that contain the same elements
c = [100, 200, 300, 400]
d = c     # Makes d an alias of c
print('Is ', c, ' equal to', d, '?')
print(c == d)

print('Are ', c, ' and ', d, ' aliases?',)
print(c is  d)