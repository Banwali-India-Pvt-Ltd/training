# THe program related to while loop statement

done = False      # Enter the loop at least once
while not done:
    entry = eval(raw_input())    # Get value from user
    if entry == 999:         # Did user provide the magic number?
        done = True          # If so, get out
    else:
        print(entry)         # If not, print it and continue