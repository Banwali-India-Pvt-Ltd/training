#debugging comprehension
# a = {1:1, 2:4, 3:4, 3:9, 4:16}\
A = {x*x: x for x in range(1, 5)if x%2 ==0}
print (A)