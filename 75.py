#  Gat the dividend and divisor from the user
dividend, divisor = eval(input('enter dividend, divisor: '))
#  we want to divide only if divisor is not zero; otherwise,
#  WE will print an error message
mdg = dividend/divisor if divisor != 0 else 'Error, cannot divide by zero'
print(msg)