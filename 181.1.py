# Chapter 9 ( List )
# Page no. 181.1

# The Program Conveniently displays the vlaues the user entered and then computes and displyas their average.

def main():
    print ("Please enter five numbers:")
    n1 = eval(input("Please enter number 1:"))
    n2 = eval(input("Please enter number 2:"))
    n3 = eval(input("Please enter number 3:"))
    n4 = eval(input("Please enter number 4:"))
    n5 = eval(input("Please enter number 5:"))
    print("Numbers entered:" , n1, n2, n3, n4, n5)     # Print all get value by users
    print("Average:", (n1 + n2 + n3 + n4 +  n5)/5)     # Addition the get value by users and Exclude average all value
main()