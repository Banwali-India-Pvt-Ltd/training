# get two integers from the user
dividend, divisor = eval(input('please enter two numbers to divide: '))
# if possible, divide them and report the tesult
if divisor != 0:
    print(dividend, '/', divisor, "=", dividend/divisor)
else:
     print('division by zero is not allowed')
     