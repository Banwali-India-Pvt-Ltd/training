from   __future__ import  print_function
for i in range(3):
    for j in range(5):
        print ("i =", i, ", j = ",j, sep="")




for i in range(1, 10):
    print ('i =', i, end=" : ")
    for j in range(1, 10):
        s_num = str(i * j)
        print (" " *(2 - len(s_num)) + s_num, end=" ")
    print ()
