s = 0  # Ok in python 3, for 2.x explicitly use a float s = 0.
for i in range(1, 11):
    n = int(input())  # Careful to only enter numbers here
    if n == -99:
        i -= 1
        break
    s += n
i = i if i else 1  # Avoids ZeroDivisionError
print 'The sum was: {}\nThe average was: {}'.format(s, s/i)
# Python program to find the sum of natural numbers up to n where n is provided by user
#https://www.programiz.com/python-programming/examples/sum-natural-number
# https://www.programiz.com/python-programming/examples/sum-natural-numberchange this value for a different result
num = 16

# uncomment to take input from the user
#num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)


