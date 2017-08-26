# We cannot change the integer
# The vaiable x in main is unaffected by increment because x reference an integer, and all integers are immutable

def increment (x):
    print("Bginning execution of increment,x=", x)     # Print x variable value- 5
    x += 1     # Add the 1  in the x variable value- 5
    print("Ending execution of increment, x=", x)     # Print x variable value- 6
def main():
    x = 5
    print("Before increment, x=", x)     # Print  x variable value- 5
    increment(x)     # Call the function ( def increment (x) )
    print("After increment, x=", x)     # Print x variable value- 5
main()     #  Start the program, and call the function ( def main() )