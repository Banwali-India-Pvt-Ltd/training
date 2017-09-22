n = raw_input("Integer? ")#Pick an integer.  And remember, if raw_input is not supported by your OS, use input()
n = int(n)#Defines n as the integer you chose. (Alternatively, you can define n yourself)
if n < 0:
    print ("The absolute value of",n,"is",-n)
else:
    print ("The absolute value of",n,"is",n)
