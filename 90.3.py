print("Help! My computer doesn't work!")
done = False
while not done:
    print("Does the coputer make any sounds (fans, etc.)")
    choice = input("or show any lights? (y/n):")
    if choice == 'n':
        choice = input ("Is it plugged in ?(y/n):")
        if choice == 'n':
            print("plug it in.")
        else:
            choice = input("Is the switch in the \"on\" position?(y/n)")
            if choice == 'n':
                print("Turn it on.")
            else:
                choice = input(" Does the computer have a fuse?(y/n):")
                if choice == 'n':
                    choice = input("Is the outtlet OK?(y/n):")
                    if choice =='n':
                        print("Check the outlets circuit ")
                        print("breaker or fuse, Move to a")
                        print("new outlet, if necessary.")
                    else:
                        print("Please consult a service technician.")
                        done = True
                else:
                    print("check the fuse. Replase if")
                    print("necessary.")
    else:
        print("Please consult a servicd technician.")
        done = True
