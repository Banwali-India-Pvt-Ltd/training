def help_screen():
    print("Add: Adds two munbers")
    print("subtracts: subtracts two munbers")
    print("print: display the result of the latest operation")
    print("help: display this help screen")
    print("Quit: exits the program")
def menu():
    return input("=== A)dd s)ubtract p)rint H)elp Q)uit ===")
def main():
    result = 0.0
    done = False;
    while not done:
        choice = menu()
        if choice == "A" or choice == "a":
            arg1 = float(input("enter arg 1: "))
            arg2 = float(input("enter arg 2: "))
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice == "s":
            arg1 = float(input("enter arg1: "))
            arg2 = float(input("enter arg2: "))
            result = arg1 - arg2
            print(result)
        elif choice == "p" or choice == "p":
            print(result)
        elif choice == "H" or choice == "h":
            help_screen()
        elif choice == "Q" or choice == "q":
            done = True
main()