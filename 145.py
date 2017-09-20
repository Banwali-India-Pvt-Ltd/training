# Displays information about how the program works
# Accept no parameters
# Returns nothing
# Not understood program
def help_screen():
    print("Add: Adds two numbers")
    print("Subtract: Subtracts two numbers")
    print("Print: Displays the result of the latest operation")
    print("Help: Displays this help screen")
    print("Quit: Exits the program")

# menu
# Display a menu
# Accepts no parameters
# Returns the string entered by the user

def menu():
    result = 0.0
    done = False;   # Initially not done
    while not done:
        choice = menu()      # Get user's choice

        if choice == "A" or choice == "a":    # Addition
            arg1 = float(raw_input("Enter arg 1: "))
            arg2 = float(raw_input("Enter ar 2: "))
            result = arg1 + arg2
            print(result)

        elif choice == "S" or choice == "s":   # Subtraction
            arg1 = float(raw_input("Enter arg 1: "))
            arg2 = float(raw_input("Enter arg 2: "))
            result = arg1 - arg2
            print(result)

        elif choice == "P" or choice == "P":   # Print
            print(result)

        elif choice == "H" or choice == "h":   # Help
            help_screen()

        elif choice == "Q" or choice == "q":   # Quit
            done = True



