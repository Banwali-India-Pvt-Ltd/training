seconds = eval(input("please enter the number of seconds:"))
hours = seconds //3600
seconds = seconds %3600
minutes = seconds //3600
seconds = seconds %3600
print (hours, "hr", minutes, "min", seconds, "sec")

