# About function
# Calculator program

# NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
# Here we will define our functions
# this prints the main menu, and prompts for a choice
def menu():
    print"Welcom to calculator.py"
    print"your options are:"
    print "1.Addition"
    print "2.Subtraction"
    print "3.Multiplication"
    print "4.Division"
    print "5.Quit calculator.py"
    return  input ("Choose your option: ")

# this adds two numbers given
def add(a,b):
    print a+b

# this subtracts two numbers given
def sub(a,b):
    print a-b

# this multiplies two numbers given
def mul(a,b):
    print a*b

# this divides two numbers given
def div(a,b):
    print a/b

#  NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "), input("to this: "))
    elif choice == 2:
        sub(input("Subtract this: "),input("from this:"))
    elif choice == 3:
        mul(input("Multiple this: "),input("by this: "))
    elif choice == 4:
        div(input("Divide this: "),input("by this: "))
    elif choice == 5:
        loop = 0
    else :
        loop=0

print"Thankyou for using calculator.py!"
# NOW THE PROGRAM REALLY FINISHES
