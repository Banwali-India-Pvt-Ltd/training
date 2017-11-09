from  __future__ import  print_function
num = 1
for i in range(0, 10):
        for j in range(10,i, -1):
            print (num,end=" ")
            num = num + 1
        print()
        num = 1