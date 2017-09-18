days = int(input("Enter days: "))
months = days / 30
days = days % 30
print("Months = %d Days = %d" % (months, days))



a = 9
b = 12
c = 3
x = a - b / 3 + c * 2 - 1
y = a - b / (3 + c) * (2 - 1)
z = a - (b / (3 + c) * 2) - 1
print("X = ", x)
print("Y = ", y)
print("Z = ", z)