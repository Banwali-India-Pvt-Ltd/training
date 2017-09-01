#flexiblesort.py
def random_list ():
    #produce a list of pseudorandom integers.
    #The list s length is chosen pseudorandomly in the
    #rang 3-20.
    #the integers in the list rang from -50 to 50
    from random import randrange
    result = []
    count = randrange(3, 20)
    for i in range (count):
        result +=[randrange(-50, 50)]
        return result
def less_than (m,n):
    return m < n
def greater_than (m, n):
    return m > n
def selection_sort(lst, cmp):
    n = len (lst)#Note i, small and j reperesent witjin lat
    #those positions
    #small is the position of the smallest value weve seen
    #so faer ; we it to find the smallest value less
    for i in range(n -1):
        small = i
        for j in range(i + 1,n):#see if smaller value can be found later in list
            if cmp(lst[j], lst[small],):
                small = j#Found a smaller value
        if i != small:#swap lst [i] and lst [small], if a smaller was foundd
            lst [i],lst [small] = lst[small],lst[i]
def main ():
    #tests the selection_sort function
    original = random_list()
    working = original[:]
    print ('original:  ', working)   #make a random list
    selection_sort(working,less_than)#make a working copy of the list
    print ('Ascending: ', working)
    working = original[:]#make a working copy of the list
    print ('original: ', working)
    selection_sort(working, greater_than)#sort descending
    print ('Descending:', working)
main()



