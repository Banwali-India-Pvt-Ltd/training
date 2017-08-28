# Chapter 7
# 7.5.4 Better Die Rolling Simulator

from random import randrange
# show_die(spots) # Draws a pictur of a die with number of spots
# indicated is tne number of spots on the top face

def show_die(spots):
    print("+--------+")
    if spots == 1:
        print("|        |")
        print("|    *   |")
        print("|        |")
    elif spots == 2:
        print("| *      |")
        print("|        |")
        print("|      * |")
    elif spots == 3:
        print("|      * |")
        print("|    *   |")
        print("| *      |")
    elif spots ==4:
        print("| *    * |")
        print("|        |")
        print("| *    * |")
    elif spots == 5:
        print("| *    * |")
        print("|    *   |")
        print("| *    * |")
    elif spots == 6:
        print("|  * * * |")
        print("|        |")
        print("|  * * * |")
    else:
        print(" *** Error: illegal die value ***")
    print("+--------+")
def roll():     # Roll  # Returns a pseudorandom number in the range 1....6
    return randrange (1, 6)
def main():     # main  # Simulates the roll of a die three times
    for i in range(0, 3):     # Roll the die three times
        show_die(roll())
main()     # Run the program