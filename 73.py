# The program prints months name on based on if/elif statements
from __future__ import print_function

month = eval(raw_input("Please enter the month as a number (1-12)"))
day = eval(raw_input("Please enter the day of the month"))

# Translate month into English
if month == 1:
    print("January ", end='')
elif month == 2:
    print("Febrauary", end='')
elif month == 3:
    print("March", end='')
elif month == 4:
    print("April", end='')
elif month == 5:
    print("May", end='')
elif month == 6:
    print("June", end='')
elif month == 7:
    print("July", end='')
elif month == 8:
    print("August", end='')
elif month == 9:
    print("September", end='')
elif month == 10:
    print("October", end='')
elif month == 11:
    print("November", end='')
elif month == 12:
    print("December", end='')

# Add the day
print(day, 'or', day, end='')

# Translate month into Spanish
if month == 1:
    print("enero")
elif month == 2:
    print("febrero")
elif month == 3:
    print("marzo")
elif month == 4:
    print("abril")
elif month == 5:
    print("abril")
elif month == 6:
    print("mayo")
elif month == 7:
    print("julio")
elif month == 8:
    print("agosto")
elif month == 9:
    print("septiembre")
elif month == 10:
    print("octubre")
elif month == 11:
    print("noviemre")
else:
    print("diciembre")
