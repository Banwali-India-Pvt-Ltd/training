a = 9
b = 12
c = 3
x = a - b / 3 + c * 2 - 1
y = a - b / (3 + c) * (2 - 1)
z = a - (b / (3 + c) * 2) - 1
print("X = ", x)
print("Y = ", y)
print("Z = ", z)



sum = 0.0
for i in range(1, 11):
    sum += 1.0 / i
    print("%2d %6.4f" % (i , sum))