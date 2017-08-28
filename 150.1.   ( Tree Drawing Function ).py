# Chapter 7
# 7.5.5 Tree Drawing Function

# Tree(height)
#     Draws a tree of a given height
# height is the height of the displayed tree
from __future__ import print_function
def tree(height):
    row = 0             # First row , from the top, to draw
    while row < height: # Draw one row for every unit of height
        count = 0       # Print leading spaces
        while count < height - row -1:
            print(end=" ")
            count += 1
        count = 0               # Print out stars, twice the current row plus one:
                                #   1. number of stars on left side of tree
                                #      = current row value
                                #   2. exactly one star in the center of tree
                                #   3. number of stars on right side of tree
                                #      = current row value
        while count < 2*row + 1:
            print(end="*")
            count += 1
        print()                 # Move cursor down to next line
        row += 1                # Change to the next row
def main():                     # main
                                #     Allows users to draw trees of various heights
    height = int(input("Enter height of tree: "))
    tree(height)
main()