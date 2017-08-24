from __future__ import  print_function
for first in 'ABCD':
    for second in 'ABCD':
        if second != first:
            for third in 'ABCD':
                if third != first and third != second:
                    for fourth in 'ABCD': #The fourth varies from A to D
                        if fourth != first and fourth != second and fourth != third:
                            print(first + second + third + fourth)