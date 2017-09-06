from random import  randrange

def random_list():
    '''
    Produce a list of pesudorandom integers.
    The list's lenght is chosen pesudorandomly in the
    range 3-20.
    The integers in the list range from -50 to 50.
    '''
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result

def selection_sort(lst):
    '''
    Arranges the elements of the lst in ascending order.
    The contents of lst are physically rearranged.
    '''
    n = len(lst)
    for i in range(n -1):
        # Note: i, small, and j represent positions within lst
        # lst[i], lst[small], and lst[j] represent the elements at
        # those positions.
        # small is the position of the smallest value we've seen
        # so far; we use it to find the smallest value less
        # than lst[i]
        small = i
        # See if a smaller value can be found later in the list
        # Consider all the elements at position j, where i < j < n
        for j in range(i + 1, n):
            if lst[j] < lst[small]:
                small = j           # Found a smaller value
        # Swap lst[i] and lst[small], if a smaller value was found
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]

def main():
    '''
    Test the selection_sort function
    '''
    for n in range(10):
        col = random_list()
        print(col)
        selection_sort(col)
        print(col)
        print('===============================')

main()