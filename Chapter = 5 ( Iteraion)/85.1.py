# Chapter -5 Iteration
# 5.1 THE WHILE STATEMENT

print("Help! My computer doesn't work!")
done = False
while not done:
    print("Does the computer make any sounds (fans, etc.) ")
    choice = input("or show any lights? (y/n):")
    if choice == 'n':
        choice = input("Is it plugged in? (y/n):")
        if choice == 'n':
            print("Plug it in.")
        else:
            choice = input("Is the switch in the \"on\" position? (y/n):")
            if choice == 'n':
                print("Turn it on.")
            else:
                choice  = input("Does the computer have a fuse? (y/n):")
                if choice == 'n':
                    choice = input("Is the outlet OK? (y/n):")
                    if choice == 'n':
                        print("check the outlet's circuit ")
                        print("breaker or fuse.  Move to a")
                        print("new outlet, if necessary. ")
                    else:
                        print("Please consult a service tecnician.")
                        done = True
                else:
                    print("Check the fuse. Replace if ")
                    print("necessary.")
    else:
        print("Please consult a service technician.")
        done = True
