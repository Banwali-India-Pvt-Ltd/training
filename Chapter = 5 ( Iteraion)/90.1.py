# Chapter -5 Iteration
# For Statement with Nested Loops

# Print a MAX x MAX multiplication table
from __future__ import print_function
MAX = 18
print(end="    ")         # First, print heading
for column in range(1, MAX + 1):    # Print column heading numbers
    print(end=" %2i " % column)
print()            # Go down to the next line

# Print line separator; a portion for each column
print(end="    +")
for column in range(1, MAX +1):
    print(end="----") # Print portion of line
print()          # Go down to the next line

# Print table contents
for row in range(1, MAX +1):     # 1 <= row <= MAX, table has MAX rows
    print(end="%2i | " % row)     # Print heading for this row.
    for column in range(1, MAX + 1): # Table has 10 colums.
        product = row*column;   # Compute product
        print(end="%3i " % product)# Display product
    print()                        # Move cursor to next row



