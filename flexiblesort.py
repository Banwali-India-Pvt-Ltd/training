def random_list():
    '''
    Produce a list of pesudorandom integers.
    The list's lenght is chosen pseudorandomly in the
    range 3-20.
    The integers in the list range from -50 to 50
    '''
    from random import  randrange
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result


def less_than(m, n):
    return m < n

def greater_than(m, n):
    return m > n


def selection_sort(lst, cmp):
    '''
    Arrange the elements of the list lst in ascending order.
    The comparer functiom cmp is used to order the elements.
    The contents of lst are physically rearranged.
    '''
    n = len(lst)
    for i in range(n - 1):
        # Note: i, small, and j represent positions within lst
        # lst[i], lst[small], and lst[j] represent the elements at
        # those positions.
        # small is the position of the smallest value we've seen
        # so far; we use it to find the smallest value less
        # than lst[i]
        small =i
        # See if a smaller value can be found later in the list
        # Consider all the elements at position j, where i < j < n.
        for j in range(i + 1, n):
            if cmp(lst[j], lst[small]):
                small = j              # Found a smaller value
        # Swap lst[i] and lst[small], if a smaller value was found
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]

def main():
    '''
    Tests the selection_sort function
    '''
    original = random_list()       # Make a random list
    working = original[:]          # Make a working copy of the list
    print('original: ', working)
    selection_sort(working, less_than)  # Sort ascending
    print('Ascending: ', working)
    working = original[:]       # Make a working copy of the list
    print('original: ', working)
    selection_sort(working, greater_than)   # Sort descending
    print('Descending:', working)

main()