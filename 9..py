# About Function

# The return statement
# Here is function name ( sum ) and parameter ( arg1, arg2 )
def sum(arg1, arg2):
    # Add both the parameters and return them.
    total = arg1 + arg2
    print"Inside the function:", total    # Print total
    return total;

total = sum (10, 20);        # Call the sum function
print"Outside the function:", total  # Print total again 
