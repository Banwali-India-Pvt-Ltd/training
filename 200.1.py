# Chapter 9
# List and Functions

def sum(lst):
                      # Adds up the contents of a list of numeric values
                      # lst is the list to sum
                      # Returns the sum of all the elements or
                      # zero if the  list is empty.

    result = 0;
    for item in lst:
        result += item
    return result
def clear (lst):
                      # Makes every element in list lst zero
    for i in range(len(lst)):
        lst[i] = 0
def random_list(n):
                      # Builds a list of n integers, where each integer is a pseudorandom number in the range 0....98.
                      # Returns the random list.
    import random
    result = []
    for i in range(n):
        rand = random.randrange(100)
        result += [rand]
    return result
def main ():
    a = [2, 4, 6, 8]
    print(a)         # Print the contents of the list
    print(sum(a))    # Compute and display sum
    clear(a)         # Zero out all the elements of list
    print(a)         # Reprint the contents of the list
    print(sum(a))    # Compute and display sum
    a = []           # Test empty list
    print(a)
    print(sum(a))
    a = random_list(10)  # Test pseudorandom list with 10 elements
    print(a)
    print(sum(a))

main()