# The program is related to Nested loops
# Print a multiplication table to 10*10
# Print a column heading

# I have doubt in this code how it actually works need to understand
from __future__ import print_function

print("    1  2 3 4 5 6 7 8 9 10")
print("   +---------------------")

for row in range(1,11):          # 1 ,= row <= 10, table has 10 rows
    if row < 10:                 # Need to add space?
        print(" ", end="")
    print(row, "| ", end="")     # Print heading for this row.
    for column in range(1, 11):  # Table has 10 columns.
        product = row*column;    # Compute product
        if product < 10:        # Need to add space?
            print(end=" ")
        if product < 101:         # Need to add another space?
            print(end=" ")
            print(product, end=" ") # Display product
    print()                      # Move to cursor to next row