# The program works on the basis of while loop
print("Help! My computer doesn't work!")
done = False   # Not done initially

while not done:
    print("Does the computer make any sounds (fans, etc.)")
    choice = raw_input("or show any light? (y/n): ")
    # The troubeshooting control logic
    if choice == 'n': # The computer does not have power
        choice = raw_input("Is it plugged in?(y/n)")
        if choice == 'n': # It is not plugged in, plug it in
            print("Plug it in")
        else:   # It is plugged in
            choice = raw_input("Is the switch in the \"on\" position? (y/n)")
            if choice == 'n':  # The switch is off, turn it on!
                print("Turn it on")
            else: # The switch is on
                choice = raw_input("Does the computer have a fuse? (y/n):")
                if choice == 'n':  # No fuse
                    choice = raw_input("Is the outlet ok? (y/n)")
                    if choice == 'n':   # fix outlet
                        print("Check the outlet circuit")
                        print("breaker or fuse. Move to a")
                        print("new outlet, if necessary")
                    else:  # Beats me!
                        print("Please consult a service technician")
                        done = True   # nothing else i can do
                else:    # check fuse
                    print("Check the fuse. replace if")
                    print("Necessary")
    else:    # The computer has power
        print("Please consult a service technician")
         # Nothing else I can do
        done = True