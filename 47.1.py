# The program uses integer division and modulus to split up
# a given number of seconds to hours, minutes, and seconds

# get the number of seconds
seconds = eval(raw_input("Please enter the number of seconds:"))
# First, compute the number of hours in the given number of seconds
hours = seconds // 3600

# Compute the remaining seconds after the hours are accounted
seconds = seconds % 3600

# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60

# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60

# print the program
print(hours, "hr", minutes, "min", seconds, "sec")