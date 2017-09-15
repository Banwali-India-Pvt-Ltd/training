# The program uses a triply-nested loop to print all the
# different arrangements of the letters A, B, and C

# The first letter varies from A to C
for first in 'ABC':
    for second in 'ABC':    # The second varies from A to C
        if second != first:   # No duplicate letters allowed
            for third in 'ABC':  # The third varies from A to C
                # Don't duplicate first or second letter
                if third != first and third != second:
                    print(first + second + third)