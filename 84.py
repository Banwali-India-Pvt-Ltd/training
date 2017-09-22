#  allow the user to enter a sequence a sequence of non-negative
#  numbers. the user ends the list with a negative
#  number.  at the end the sum of the sum of the non-negative
#  numbers entered is displayed. the program prints
#  zero if fhe user provides no non-negative numbers

entry = 0   # ensure the loop is entered
sum  = 0    # initialize syum

#  request input from the user
print("enter numbers to sum, negative number ends list: ")

while entry >= 0:           # a negative number exits the ioop
    entry = eval(input())   # get the value
    if entry >= 0:          # is number non-negative
        sum  += entry       # only add it if it is non-negative
print("sum =", sum)         # display the sum