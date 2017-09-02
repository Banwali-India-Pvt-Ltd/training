
#Returns the index of element seek in list lst,
4 #if seek is present in lst.
5 #lst must be in sorted order.
6 #Returns None if seek is not an element of lst.
7# lst is the lst in which to se
def binary_search(lst, seek):
    first = 0# Initially the first element in list
    last = len(lst) -1
    last = len(lst) - 1
    while first <= last:#mid is middle of the list
        mid = first + (last - first + 1)//2#note:integer division
        if lst[mid] == seek:
            return mid    #found if
        elif lst[mid] > seek:
            last = mid - 1     #continue with lst half
        else:
            fist = mid + 1
    return None
def ordered_linear_search(lst,seek):
    i = 0
    n = len(lst)
    while i < n and lst[i] <= seek:
        if lst [i] ==seek:
            return i
        i += 1
    return None
def test_searches(lst):
    from time import clock
    start = clock()
    n = len(lst)
    #find each element using binary search
    for i in range(n):   #start the ciock
        if ordered_linear_search(lst,i) !=i:
            print ("error")
    stop = clock()      #stop the clook
    print ("Binary elapsed time", stop - start)
def main():
    SIZE = 20000
    test_list = list(range(SIZE))
    test_searches(test_list)
main ()



