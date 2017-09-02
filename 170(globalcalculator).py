def help_screen():
    print("Add: Adds two numbers")
    print("Subtract: Subtract two numbers")
    print("Print: Displays the result of the latest operation")
    print("Help: Displays this help screen")
    print("Quit: Exits the program")
def manu():
    return input("=== A)dd s)ubtract p)rint H)elp Q)uit ===")
result = 0.0
arg1 = 0.0
arg2 = 0.0
def get_input():
    global arg1, arg2
    arg1 = float(input("enter argument #1: "))
    arg2 = float(input("enter argument #2: "))
def report():
    print(result)
def add():
    global result
    result = arg1 + arg2
def subtract():
    global result
    result = arg1 - arg2
def main():
    done = False;
    while not done:
     choice = manu()
     if choice == "A" or choice == "a":
         get_input()
         add()
         report()
     elif choice == "S" or choice == "s":
         get_input()
         subtract()
         report()
     elif choice == "P" or choice == "p":
         report()
     elif choice == "H" or choice == "h":
         help_screen()
     elif choice == "Q" or choice == "q":
         done = True

main()




