# The program implements a conditions steps by steps

print("Help! My computer doesn't work!")
print("Does the computer make an sounds (fans, etc.)")

choice = raw_input("or show any lights? (y/n):")
# The trouleshooting control logic
if choice == 'n':  # The computer does not have power
    choice = raw_input("Is it plugged in? (y/n):")
    if choice == 'n':  # It is plugged in, plug it in
        print("Plug it in. if the problem persists,")
        print("please run this program again.")

    else:   # It is plugged in
        choice = raw_input("Is the switch in the \"on\" position? (y/n): ")
        if choice == 'n':   # The switch is off, turn is on!
            print("Turn it on. If the problem persists,")
            print("Please run this program again.")

        else:  # The switch is on
            choice = raw_input("Does the computer hava a fuse? (y/n:")
            if choice == 'n': # No fuse
                choice = raw_input("Is the outlet OK? (y/n):")
                if choice == 'n':   # Fix outlet
                    print("Check the outlet's circuit")
                    print("breaker or fuse. Move to a")
                    print("new outlet, if necessary.")
                    print("if the problem persists, ")
                    print("Please run this program again.")
                else:  # Beats me!
                    print("Please consult a service technicain.")
            else:   # Check fuse
                print("Check the fuse. Replace if")
                print("necessary. If the problem")
                print("Persists, then")
                print("please run this program again.")
else:    # The computer has power
    print("Please consult a service technicain.")
