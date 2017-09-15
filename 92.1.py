# The program keep condition of break statement
# The program have abnormal loop termination

print("Help! My computer doesn't work!")
while True:
    print("Does the computer make any sounds (fans, etc.)")
    choice = raw_input(" or show any lights? (y/n):")
    # The troubleshooting control logic
    if choice == 'n':  # The computer does not have power
        choice = raw_input("Is it plugged in? (y/n):")
        if choice == 'n':   # It is not plugged in, plug it in
            print("plug it in.")
        else:  # The switch is on
            choice = raw_input("Does the computer have a fuze? (y/n): ")
            if choice == 'n':   # No fuse
                choice = input("Is the outlet ok? (y/n):")
                if choice == 'n':    # fix outlet
                    print("Check the outlet circuit")
                    print("Breaker or fuse. move to a")
                    print("new outlet, if necessary.")
                else:    # beats me!
                    print("Please consult a service technician.")
                    break   # Nothing else I can do, exit loop
            else:   # check fuse
                print("Check the fuse. Replace if")
                print("necessary.")
    else:   # The computer has power
        print("Please consult a service technician.")
        break    # Nothing else I can do, exit loop

