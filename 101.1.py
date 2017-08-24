entry = 0
sum = 0
print("enter numbers to sum, negative number ends list:")
while True :
    entry = eval(input())
    if entry < 0:
        break
        sum += entry
        print("sum =", sum)
        