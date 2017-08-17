# Chapter -3 Expressions and Arithmetic
# ARITHMETIC EXAMPLES

seconds = eval(input("Please enter the number of seconds:"))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print (hours, "hr,", minutes, "min,", seconds, "sec")
