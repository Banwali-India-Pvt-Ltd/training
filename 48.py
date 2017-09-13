# Get the number of seconds

from __future__ import print_function
seconds = eval(raw_input("Please enter the number of seconds:"))

# First, compute the number of hours in the given number of seconds
hours = seconds // 3600   # 3600 seconds = 1 hours

# Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600

# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60 # 60 seconds = 1 minute

# compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60


# print the results
print(hours, ":", sep="", end="")

# Compute tens digit of minutes
tens = minutes // 10

# Compute one digit of minutes
ones = minutes % 10

print(tens, ones, ":", sep="", end="")

# Compute tens digit of seconds
tens = seconds // 10

# Compute ones digit of seconds
ones = seconds % 10

print(tens, ones, sep ="")