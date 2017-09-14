# The program takes an input from user and print line text
from __future__ import print_function
val = eval(raw_input())
if val < 10:
    if val != 5:
        print("wow", end="")
    else:
        val += 1
else:
    if val == 17:
        val += 10
    else:
        print("whoa", end='')
print(val)
