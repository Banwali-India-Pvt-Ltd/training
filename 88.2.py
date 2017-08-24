from __future__ import  print_function
val = eval(input("Entry integer numbers "))
if val < 10:
    if val != 5:
        print ("wow ",end='')
    else:
        val += 1
else:
    if val == 17:
        val += 10
    else:
        print("whoa ", end='')
print(val)