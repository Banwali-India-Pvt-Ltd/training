#globalcalcalator .py
#help_screen
#Displays information about how the program works
#Accepts no parameters
#Returns nothing
def help_screen ():
    print ("Add: Add two numbers")
    print ("Subtrct: Subtracts two numbers")
    print ("Print: Displays this result of the lates operation")
    print ("Help: Displays this help screen")
    print ("Quit: Exits the program")
    #mena
    #Display a menu
    #Accepts no parameters
    #Returns the string entered by the user
def menu ():
#display a menu
    return input("=== A")
result = 0.0
arg1 = 0.0
arg2 = 0.0
def get_input():
    global arg1, arg2 #arg1 and arg2 are globals
    arg1 = float (input("Enter argument #1: "))
    arg2 = float (input("Enter argument #2: "))
    #report
    #Reportsthe value of the global result
def report():
    #Not assigning to result global keyword not needed
    print (result)
    #add
    #Assigns the sum of the globals  arg1 and arg2
    def add ():
     global  result
    result = arg1 + arg2
def subtract ():
     global result
     result = arg1 - arg2
def main ():
    done = False;
    while not done:
          choice = menu ()
          if choice == "A" or choice == "a":
             get_input()
             add()
             report()
          elif choice == "S" or choice == "s":
             get_input()
             subtract()
             report()
         elif choice  == "P" or choice == "p":
               report()
         elif choice == "H"  or choice =="h:"
         help_screen()
         elif choice == "Q" or choice == "q":
           done = True
main()






