from random import randrange# file name is sortintegers.pr
def random_list():
    result = []   #produce a list of pseudorandom integers.
    count = randrange (3, 20)#the list's length is chosen pseudorandomly in
    for i in range(count):#rang 3-20
        #the integers in the list range from -50 to 50.
        result += [randrange(-50, 50)]
        return result
def selection_sort(lst):#Arran the elements of list lst in ascending order
    n = len(lst)#the  contents of lst physically rearranged.
    for i in range(n-1):# note:i, small and j and lst[j] represent the smallest
        small = i#see if a smaller value can be found later in the list
        #consider all the elements at positionj, where i<j<n
        for j in range(i + 1,n):
            if lst[j]<lst[small]:
                small =j
                #found a smaller value
                #swap lst [i] and lst [ssmall],if a smaller value was found
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]
def main ():
    for n in range(10):
        col = random_list()
        print (col)
        selection_sort(col)
        print (col)
        print ('==== ===== ===== ====== =======')
main()




