# About function


# This code print month name with if, elif statement in function
# Here is a function name ( MonthName ) and parameter
def MonthName(a):      # Here is function name (MonthName) and a parameter
   # Check the variables ( a ) value and difine a Month name
    if a == 1:
        print"Month:-> January"
    elif a == 2:
        print"Month:-> February"
    elif a == 3:
        print"Month:-> March"
    elif a == 4:
        print"Month:-> April"
    elif a == 5:
        print"Month:-> May"
    elif a == 6:
        print"Month:-> June"
    elif a == 7:
        print"Month:-> July"
    elif a == 8:
        print"Month:-> Augest"
    elif a == 9:
        print"Month:-> September "
    elif a == 10:
        print"Month:-> October"
    elif a == 11:
        print"Month:-> November"
    elif a == 12:
        print"Month:-> December"
    else:
        print"Not Month of Name"
    print"Year of:-> 2017"        # Print year

a = 1                 # Chang the a variable value and find  latest a month name
print MonthName(a)                # Call the function and start program
