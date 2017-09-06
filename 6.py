# About Functions

# Pass by reference vs value
# Function definition is here
def changme(mylist):    # Here is a function name ( changme ) and parameter ( mylist)
    "This change a passed list into this function"
    mylist = [1, 2, 3, 4];          # This would assign new reference
    print"Value inside the function:", mylist
    return

mylist = [10, 20, 30];
changme(mylist);
print"Value outside the function:", mylist   # Call the function