def permute(prefix, suffix):
    '''
    Recursively shifts all the elements in suffix into
    prefix producing all the permutations of suffix.
    prints all permutations in lexicographical order.
    '''
    suffix_size = len(suffix)
    if suffix_size == 0:    # Have we considered all the elements?
        print(prefix)
    else:
        for i in range(0, suffix_size):
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i + 1:]
            permute(new_pre, new_suff)



def print_permutations(lst):
    '''
    Calls the recursive permute function to display
    all the permutations of elements of lst in
    lexicographical order. The empty list is passed as
    the first parameter to permute, and the list to
    permute is passed as the second argument.
    '''
    permute([], lst)

def main():
    a = [1, 2, 3, 4]
    print_permutations(a)

main()