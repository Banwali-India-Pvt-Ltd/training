from __future__ import  print_function
hight = eval(input("enter hight of tree: "))
row = 0
while row < hight:
    count = 0
    while count < hight - row -1 :
        print(end=" ")
        count += 1
    count = 0
    while count < 2*row + 1:
      print(end="*")
      count +=1
    print()
    row += 1
