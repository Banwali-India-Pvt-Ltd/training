from __future__ import  print_function
a = 0
while a < 1100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
            b += 1
            print()
            a += 1