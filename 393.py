invalid = True
while invalid:
    number = int(input("Please enter a number in the range 10 to 20: "))
    if number >= 10 and number <= 20:
        invalid = False
    else:
        print("Sorry number must be between 10 and 20")
        print("Please try again")
print("You entered {0}".format(number))
print("This is a valid number")