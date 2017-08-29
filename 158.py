from random import randrange
#indicted spots is the number of spots of the top face
def show_die (spots):
    print ("+--------+")
    if spots == 1:
        print ("|        |")
        print ("|    *   |")
        print ("|        |")
    elif spots == 2:
        print ("| *      |")
        print ("|        |")
        print ("|       *|")
    elif spots == 3:
        print ("|      * |")
        print ("|    *   |")
        print ("| *      |")
    elif spots == 4:
        print ("| *     *|")
        print ("|        |")
        print ("| *     *|")
    elif spots == 5:
        print ("| *     *|")
        print ("|    *   |")
        print ("| *     *|")
    elif spots == 6:
        print ("| *  *  *|")
        print ("|        |")
        print ("| *  *  *|")
    else:
        print (" *** Error illegal die value ***")
    print ("+--------+")
    #roll
    #returns a pseudorandom number in the rang 1....6
def roll():
    return randrange (1,6)
    #main
def main():
    # type: () -> object
    #roll the die three times
    for i in range(0, 3):
        show_die(roll())
main() #run the program
