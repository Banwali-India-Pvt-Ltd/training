from  __future__ import  print_function
num = int(input("enter the number of rows:"))
for i in range(num,0,-1):
    for j in range(0,i):
        print ("*",end="")
    print()
