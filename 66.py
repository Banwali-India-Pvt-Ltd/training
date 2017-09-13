a, b = 0, 1
while b < 100:
    print(b,)
    a, b = b, a + b

 # !/usr/bin/env python3
x = float(raw_input("Enter the value of x: "))
n = term = num = 1
sum = 1.0
while n <= 100:
    term *= x / n
    sum += term
    n += 1
    if term < 0.0001:
     print ("no of Times= %d and sum= %f" % (n, sum))