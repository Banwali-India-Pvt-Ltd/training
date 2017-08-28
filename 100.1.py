from __future__ import  print_function
#file enhancedtimeconv .py
#get the number of seconds
seconds = eval(input("please enter the number the number of seconds"))
#first, compute the number of hours in the number of hours in the given number of seconds
#Note :intrger division with possible truncation
hours = seconds //3600 #3600 seconds = 1 hours
# compute the remainig seconds after the hours are accountedfor
seconds = seconds % 3600
#next compute the number of minutes in the remaning numberof accounted for
minutes = seconds //60
#comoute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
#repoet the results
print (hours, ":", sep=" ", end=" ")
tens = minutes //10
#compute ones digit of minutes
ones = minutes % 10
print (tens, ones,":", sep=" ", end=" ")
tens = seconds //10
#compute tens digit of seconds
ones = seconds % 10
print (tens, ones, sep=" ",)