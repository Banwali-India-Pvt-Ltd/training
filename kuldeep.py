from __future__ import print_function
second = eval(input("please enter the number of seconds:"))
hours = second // 3600
second = second % 3600
minutes = second // 60
second = second % 60
print (hours, ":", sep=" ", end=" ")
tens = minutes // 10
ones = minutes % 10
print (tens, ones, ':', sep=" ", end=" ")
tens = second % 10
print (tens, ones, sep=" ")







