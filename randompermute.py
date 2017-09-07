from random import  randrange

def permute(lst):
    '''
    Randomly permute the contents of list lst
    '''
    n = len(lst)
    for i in range(n - 1):
        pos = randrange(i, n)      # i <= pos < n
        lst[i], lst[pos] = lst[pos], lst[i]

def main():
    '''
    Tests the permute function that randomly permute the
    contents of a list
    '''
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Before:', a)
    permute(a)
    print('After :', a)

main()