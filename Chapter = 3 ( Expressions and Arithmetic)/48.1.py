# Chapter -3 Expressions and Arithmetic
# 3.7 ALGORITHMS


seconds = eval(input("Please enter the number of seconds:"))ss
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print (hours, ":", sep="", end="")
tens = minutes // 10
ones = minutes % 10
print (tens, ones, ":", sep="", end="")
tens = seconds // 10
ones = seconds % 10
print(tens, ones, sep ="")