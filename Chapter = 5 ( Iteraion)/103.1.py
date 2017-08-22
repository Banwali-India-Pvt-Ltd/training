# Chpater -5 Iteration
# 5.7.2 Drawing a Tree

from __future__ import print_function
height = eval(input("Enter height of tree: "))
row = 0
while row < height:
    count = 0
    while count < height - row -1:
        print(end=" ")
        count += 1
    count = 0
    while count < 2*row +1:
        print(end="*")
        count += 1
    print()
    row += 1
