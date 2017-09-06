# About function

# Scope of Variables
# Global vs. Local variables

total = 0;   # This is global variable.
def sum ( arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2;       # Here total is local variable
    print"Inside the function local total:", total    # Print total
    return total;

sum (10, 20) # Call the function
print"Outside the function global total:", total