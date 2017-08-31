# Chapter 10
# 10.1 Sorting

from random import randrange

def random_list():    # Produce a list of pseudorandom integers.
                      # The lsit's length is chosen pseudorandmly in the rnage 3-20.
                      #  The integers in the list rangne from -50 to 50.
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result
def selection_sort(lst):
                           # Arranges the elements of list lst in ascending order.
                           # The contents of lst are physically rearranged.
    n = len(lst)
    for i in range(n - 1):
                           # Note: i, small, and j represent positions within lsit
                           # lst[i], lst[small], and lst[j] represent the elements at those positions.
                           # small is the position of the smallest value we've seen
                           # so far; we use it to find the smallest value less than lst[i]
        small = i
        for j in range (i + 1, n):
                                       # See if a smaller value can be found later in the list
                                       # Consider all the elements at position j, where i < j < n
            if lst[j] < lst[small]:
                small = j              # Found a smaller value
        if i != small:            # Swap lst[i] and lst[small], if a smaller value was found
            lst[i], lst[small] = lst[small], lst[i]
def main():
    for n in range(10):     # Tests the selection_sort function
        col = random_list()
        print(col)
        selection_sort(col)
        print(col)
        print('========================================')

main()