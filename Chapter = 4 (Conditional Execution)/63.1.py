# Chapter -4 Conditional Execution
# 4.4 The if/else Statement

dividend, divisor = eval(input('Please enter two numbers to divide: '))
if divisor != 0:
    print(dividend, '/', divisor, "=", dividend/divisor)
else:
    print('Division by zero is not allowed')
