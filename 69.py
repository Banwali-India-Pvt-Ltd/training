value = eval(input("please enter an integer value in the range 0_ _ _10: "))
if value >= 0:    # first check
    if value <=10: # second check
        print(value, "is in range")
    else:
        print(value, "is too large")
else:
     print(value, "is too small")
print("done")

