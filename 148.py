from random import randrange

# show_die(spots)
#    Draws a picture of a die with number of spots
#    indicated spots is the number of spots on the top face

def show_die(spots):
    print("+--------+")
    if spots == 1:
        print("|      |")
        print("|  *   |")
        print("|      |")

    elif spots == 2:
        print("| *    |")
        print("|      |")
        print("|    * |")

    elif spots == 3:
        print("|    *  |")
        print("|   *   |")
        print("| *     |")

    elif spots == 4:
        print("| *  *  |")
        print("|       |")
        print("| *  *  |")

    elif spots == 5:
        print("| *  *  |")
        print("|  *    |")
        print("| *  *  |")

    elif spots == 6:
        print("| * * * |")
        print("|       |")
        print("| * * * |")

    else:
        print(" *** Error: illegal die value ***")
    print("+-------+")

# roll
# Returns a pseudorandom number in the range 1....6

def roll():
    return randrange(1, 6)

# main
#   Simulates the roll of a die three times
def main():
    # Roll the die three times
    for i in range(0, 3):
        show_die(roll())

main()     # Run the program

