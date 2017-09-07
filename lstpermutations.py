from __future__ import  print_function
def permute(prefix, suffix, depth):
    '''
    Recursively shifts all the elements in suffix into
    prefix producing all the permutations of suffix.
    Prints all permutations in lexicographical order.
    '''
    suffix_size = len(suffix)
    if suffix_size == 0:    # Have we considered all the elements?
        pass # print('>>>', prefix, '<<<')
    else:
        for i in range(0, suffix_size):
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i + 1:]
            tab(depth)
            print(new_pre, new_suff, sep=' : ')
            print(new_pre, new_suff, depth + 1)
def tab(n):
    for i in range(n):
        print(end='   ')
permute([], [1, 2, 3, 4], 0)

