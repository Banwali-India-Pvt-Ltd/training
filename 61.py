# The program returns a boolean expressions
# Get two integers from the user

dividend, divisor = eval(raw_input('Please enter two numbers to divide:'))

# if possible, divide them and report the result

if divisor != 0:
    quotient = dividend/divisor
    print(dividend, '/', divisor, "=", quotient)

    print('Proram finished')