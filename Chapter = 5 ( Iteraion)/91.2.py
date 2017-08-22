# Chapter -5 Iteration
# 5.3. The For Statement

for first in 'ABCD':
    for second in 'ABCD':
        if second != first:
            for third in 'ABCD':
                if third != first and third!= second:
                    for fourth in 'ABCD':
                        if fourth != first and fourth != second and fourth != third:
                            print(first + second + third + fourth)
