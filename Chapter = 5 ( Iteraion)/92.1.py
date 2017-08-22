# Chapter -5 Iteration
# 5.5.1  The break statement

entry = 0
sum = 0
print("Enter numbers to sum, nagative number ends list:")
while True:
    entry = eval(input('r'))
    if entry < 0:
        break
    sum += entry
print("Sum =", sum)