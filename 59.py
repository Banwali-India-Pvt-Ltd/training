# The program returns simplest if statement
# First get two integers from the user

dividend, divisor = eval(raw_input('Please enter two numbers to divide:'))

# if possible, divide them and report the result

if divisor != 0:
    print(dividend, '/', divisor, '=', dividend/divisor)