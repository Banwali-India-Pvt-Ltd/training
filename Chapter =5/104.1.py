# Chapter -5 Iteration
# Drawing a Tree

from __future__ import print_function
height = eval(input("Enter height of tree: "))
for row in range(height):
    for count in range(height - row):
        print(end=" ")
    for count in range(2*row + 1):
        print(end="*")
    print()