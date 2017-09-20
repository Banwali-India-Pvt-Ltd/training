# tree(height)
# Draws a tree of a given height
# height is the height of the displayed tree
from __future__ import print_function

def tree(height):
    row = 0      # First row, from top, to draw
    while row < height: # Draw one row for every unit of height

     count = 0
     while count < height - row:
        print(end=" ")
        count += 1

    # Print out stars, twice the current row plus one:
        # 1. number of stars on left side of tree
        #     = currently row value
        # 2. exactly one star in the center of tree
        # 3. number of stars on right side of tree
        #     = current row value

        count = 0
        while count < 2*row + 1:
            print(end="*")
            count += 1
        # Move cursor down to next line
        print()
        # Change to the next row
        row += 1

# main
# Allows users to draw trees of various heights

def main():
    height = int(raw_input("Enter height of tree: "))
    tree(height)

main()