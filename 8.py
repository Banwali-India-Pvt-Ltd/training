# About function

# About Variables length Arguments
def printinfo(arg1, * vartuple):  # Here is a function name (printinfo) and a parameter ( arg, * vartuple)
    "This prints a variable passed argument."
    print "Output is :"
    print arg1
    for var in vartuple:
        print var
    return

printinfo(10)          # Call the function
printinfo(70, 60, 50)  # Call the function again