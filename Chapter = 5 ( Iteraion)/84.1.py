# Chapter 5 Iteration
# 5.1 THE WHILE STATEMENT

entry = 0
sum = 0
print("Enter numbers to sum, negative number ends list:")
while entry >= 0:
    entry = eval(input('Enter a integer number?:'))
    if entry >= 0:
        sum += entry
print("Sum =", sum)
