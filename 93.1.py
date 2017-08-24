entry = 0
sum = 0
print ("enter numbers to sum, negative number ends list: ")
while entry >= 0:
    entry = eval(input())
    if entry >= 0:
        sum += entry
        print ("sum =", sum)
