def main():
    print("please enter five numbers: ")
    # Allow the user to enter in the five values.
    n1 = eval(input("please enter number 1: "))
    n2 = eval(input("please enter number 2: "))
    n3 = eval(input("please enter number 3: "))
    n4 = eval(input("please enter number 4: "))
    n5 = eval(input("please enter number 5: "))
    print("numbers entered:", n1, n2, n3, n4, n5)
    print("Average:", (n1 + n2 + n3 + n4 + n5)/5)
main()