#!/usr/bin/env python3
sum = 0.0
for i in range(1, 11):
    sum += 1.0 / i
    print("%2d %6.4f" % (i , sum))

    # !/usr/bin/env python
    import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = b * b - 4 * a * c
if d < 0:
    print "ROOTS are imaginary"
else:
    root1 = (-b + math.sqrt(d)) / (2.0 * a)
    root2 = (-b - math.sqrt(d)) / (2.0 * a)
    print("Root 1 = ", root1)
    print("Root 2 = ", root2)