from  __future__ import print_function
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and(col>0)):
            print ("*",end="")
        else:
            print (end=" ")
    print ()





for row in range(10):
    for col in range(10):
        if (row==3) or (col==0) or  (row==4  or row==6)and (col>0):
            print ("*", end="")
        else:
            print (end=" ")
    print ()


