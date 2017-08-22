# Chapter -5 Iteraion
# 5.5.1. The break statement

print("Help! My computer doesn't work!")
while True:
    print("Does the computer make any sounds (fans, tec.)")
    choice = input(" or show any lights? (y/n):")
    if choice == 'n':
        choice = input("Is it plugged in? (y/n):")
        if choice == 'n':
            print("Plug it in.")
        else:
            choice = input("Is the switch in the \"on\" position? (y/n):")
            if choice == 'n':
                print("True it on.")
            else:
                choice = input("Does the computer have a fuse? (y/n):")
                if choice == 'n':
                    choice = input("Is the outlet OK? (y/n):")
                    if choice == 'n':
                        print("Check the outlet's circuit ")
                        print("breaker or fuse. Move to a")
                        print("new outlet, if necessary. ")
                    else:
                        print("Please consult a service technician.")
                        break
                else:
                    print("Check the fuse. Replace if ")
                    print("necessary.")
    else:
        print("Please consult a service technician.")
        break