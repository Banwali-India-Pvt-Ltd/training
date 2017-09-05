from __future__ import  print_function
def main():
    # Set up variables
    sum = 0.0
    NUMBERS_OF_ENTRIES = 5
    numbers = []

    #  Get input from user
    print("please enter", NUMBERS_OF_ENTRIES, "numbers: ")
    for i in range(0, NUMBERS_OF_ENTRIES):
        num = eval(input("enter number " + str(i) + ": "))
        numbers += [num]
        sum += num;

        # Print the numbers entered
    print(end="numbers entered: ")
    for num in numbers:
        print(num, end=" ")
    print()          # Print newline

            # Print average
    print("Average:", sum/NUMBERS_OF_ENTRIES)

main()    # Execute main
