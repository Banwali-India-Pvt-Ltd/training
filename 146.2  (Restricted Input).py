# Chapter -7 Writing Functions
# 7.5.3 Restricted Input

# get_int_in_range(first, last)
# Forces the user to enter an integer within a
# Specified range
# First is either a minimum or maximum acceptalbe value
# Last is the corresponding other end of the range
# Either a maximum or minimum value
# Returns an acceptable value from the user

def get_int_in_range(first, last):
    if first > last:     # If the larger number is provided first, # Switch the parameters
        first, last = last, first
# Insist on value in the range first...last
    in_value = int(input("Please enter values in the range " "\" "  + str(first) + "..." + str (last) + ":" ))
    while in_value < first or in_value > last:
        print(in_value, "is not in the range", first, "...", last)
        in_value = int(input("Please try again: "))
    return in_value;     # in_value at this point is guarnteed to be within range
def main():     # main  # Tests the get_int_in_range function
    print(get_int_in_range(10,20))
    print(get_int_in_range(10,20))
    print(get_int_in_range(5,5))
    print(get_int_in_range(-100,100))
main()     # Run the program
