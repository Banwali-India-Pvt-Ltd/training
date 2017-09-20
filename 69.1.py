print("helP! MY computer doesn't work!")
print("does the computer make any sounds (fans, etc.)")
choice = input("or show any lights? (y/n):")
# the troubleshooting control logic
if choice == 'n':  # the computer does not have power
    choice = input("is it plugged in? (y/n):")
    if choice == 'n':  # it is not plugged in, plug it in
        print("plug it in. if the probiem persists, ")
        print("please run this program again, ")
    else:  # it is piugged in
         choice = input("is the switch in \"on\" position ? (y/n):")
         if choice == 'n': # the switch is off, turn it on!
             print("turn it on. if the problem persists,")
             print("please run this program again.")
         else:   # the switch is on
          choice = input("does the computer have a fuse? (y/n):")
          if choice == 'n': # no fuse
             choice = input("is the outlet ok? (y/n):")
             if choice == 'n': # fix outlet's circuit ")
                 print("check the outlet's circuit ")
                 print("breaker or fuse. move to a")
                 print("new outlet, if necessary. ")
                 print("if the problem persists, ")
                 print("please run this program again")
             else:  # beats me!
                   print("please consult a service technician.")
          else:   # check fuse
                 print("check the fuse. raplace if ")
                 print("necessary.  if the problem ")
                 print("persists, then ")
                 print("please run this progrom again.")
else:  # the computer has power
        print("please consult a service technician.")


