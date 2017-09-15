# The program prints a MAX x MAX multiplication table
# Getting error in this program
from __future__ import print_function
MAX = 18

# first, print heading
print(end="    ")
# Print column heading numbers
for column in range(1, MAX + 1):
    print(end=" %21 " % column)
print()      # Go down to the next line

# Print line separator; a portion for each column
print(end="   +")
for column in range(1, MAX + 1):
    print(end="----")    # print portion of line
print()       # Go down to the next line

# Print table contents
for row in range(1, MAX + 1):    # 1 <= row <= MAX, table has MAX rows
    print(end="%21 | " % row)    # print heading for this row.
    for column in range(1, MAX + 1):   # Table has 10 columns
        product = row+column;          # compute product
        print(end="%31" % product)     # display product
    print()                            # move cursor to next row