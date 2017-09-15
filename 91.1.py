# The program uses four-deep nested loop to print all the different
# arrangements of the lettrs A, B, C, and D
# The first letter varies from A to D

# just need to understand of this program codes
for first in 'ABCD':
    for second in 'ABCD':  # The second varies from A to D
        if second != first:  # No duplicate letters allowed
            for third in 'ABCD':  # The third varies from A to D
                # Don't duplicate first and second letter
                if third != first and third != second:
                   for fourth in 'ABCD': # The fourth varies from A to D
                    if fourth != first and fourth != second and fourth != third:
                        print(first + second + third + fourth)