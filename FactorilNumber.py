def factorial(x):
    result = 1
    while(x>=1):
        result = result * x
        x = x-1
    return result
x = int(raw_input("Enter a number"))
print(factorial(x))

import math
print(math.factorial(5))