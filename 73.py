from __future__ import print_function
month = eval(input("please enter the month as a nonth: "))
day = eval(input("please enter the day of the month: "))
# translate month into english
if month == 1:
    print("january ", end='')
elif month == 2:
    print("february ", end='')
elif month == 3:
    print("march ", end='')
elif month == 4:
    print("april ", end='')
elif month == 5:
    print("may ", end='')
elif month == 6:
    print("june ", end='')
elif month == 7:
    print("july ", end='')
elif month == 8:
    print("august ", end='')
elif month == 9:
    print("septemder ", end='')
elif month == 10:
    print("october ", end='')
elif month == 11:
    print("november ", end='')
else:
    print("december ", end='')
# add the day
print(day, 'or', day, end='')
#  translate month into spanish
if month == 1:
    print(" enero")
elif month == 2:
    print(" febrero")
elif month == 3:
    print(" marzo")
elif month == 4:
    print(" abril")
elif month == 5:
    print(" mayo")
elif month == 6:
    print(" junio")
elif month == 7:
    print(" julio")
elif month == 8:
    print(" agosto")
elif month == 9:
    print(" septiembre")
elif month == 10:
    print(" octubre")
elif month == 11:
    print(" noviembre")
else:
    print(" diciembre")