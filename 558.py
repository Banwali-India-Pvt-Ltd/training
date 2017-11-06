from  __future__ import print_function
for row in range(7):
    for col in range(5):
        if col==0  or col==4or (row==3 and(col>0and col<4)):
           print ("*",end="")
        else:
            print(end=" ")
    print()


