# Chapter 9 ( List )
# Page No. 182.1

# This program showing the get the value exclude the average
def main():
    sum = 0.0
    NUMBER_OF_ENTRIES = 5
    print ("Please enter", NUMBER_OF_ENTRIES , "numbers: ")
    for i in range(0, NUMBER_OF_ENTRIES):    # Loops running five times
        num = eval(input("Enter number " + str(i) + ": "))     # Get the value by users
        sum += num;
    print("Average:", sum/NUMBER_OF_ENTRIES)     # Addition the value get by users and Exclude the average all value
main()