# The program checks weather the value is in range or not
# here used nested if and else condition

# leave message user to enter value
value = eval(raw_input("Please enter an integer value in the range 0...10:"))
if value >= 0:    # first check
    if value <=10:   # second check
        print(value, "is in range")

    else:
        print(value, "is too large")

else:
    print(value, "is too small")




