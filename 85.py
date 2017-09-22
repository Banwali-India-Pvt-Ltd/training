from __future__ import print_function
print("help!  my computer doesn't work!")
done = False    # not done initially
while not done:
    print("does the computer make any sounds (fans, etc.")
    choice = input("or show any lights? (y/n):")
    #    the troubleshooting control logic
    if choice == 'n': #  the computer does not have power
        choice = input("is it plugged in? (y/n):")
        if choice == 'n': # it is not plugged in, plug it in
           print("plug it in.")
        else:   # it is plugged in
            choice == input("is the switch in the \"on\" position? (y/n):")
            if choice == 'n':  #  the switch is off, turn it on!
                print("turn it on.")
            else:   # the switch is on
                choice = input("does the computer have a fuse?  (y/n): ")
                if choice == 'n':   # no fuse
                    choice = input("is the outlet ok? (y/n): ")
                    if choice == 'n' : #  fix outlet
                     print("check the outlet's circit ")
                     print("breaker or fuse. move to a")
                     print("nuw outlet, if necessary. ")
                else:  # beats me!
                    print("please consult a service technician.")
                    done = True   # NOthing else i can do
    else:#  check fuse
        print("check the fuse.replace if ")
        print("necessary.")
else:   # the computer has power
    print("please consult a service technician.")
    done = True     # nothing else i can do