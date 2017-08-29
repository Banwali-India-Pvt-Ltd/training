def main():
    sum = 0.0     # Set up variables
    NUMBER_OF_ENTRIES = 5
    numbers = []
    print("Please enter", NUMBER_OF_ENTRIES, "numbers: ")     # Get input from user
    for i in range(0, NUMBER_OF_ENTRIES):
        num = int(input("Enter number " + str(i) + ":"))
        numbers += [num]
        sum += num;
    print("Numbers entered: ")     # Print the numbers entered 0
    for num in numbers:
        print(num)
    print()     # Print newline
    print("Average:", sum/NUMBER_OF_ENTRIES)     # Print average
main()     # Execute main