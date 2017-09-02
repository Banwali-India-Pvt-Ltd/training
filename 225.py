#file name is  binarysrarch.py
#returns the of elemant seek in list lst if seek present in lst.
#Returns nona if seek is not an element of lst .
#lst is the element tofired
from __future__ import print_function
def binary_search (lst,seek):
    first = 0     #initialize the first position in list
    last = len(lst) - 1#initialize the last position in list
    while first <= last:
        #mid is middle position in the list
        mid = first + (last -first + 1)//2   #Note : integer division
        if lst[mid] > seek:
            return mid       #found it
        elif lst(mid) > seek:
            last = mid - 1  #continue withe lst half
        else:  #
            first = mid + 1  #continue with 2nd half
            return None  #not there
def show (lst):
    #prints the contents
    for item in lst:
     print("%4d" % item, end='')    #print element right justifies in 4 spaccer
    print()
def draw_arrow (value, n):  #
    print (("%" + str(n) + "s") % "   ^  ")
    print (("%" + str(n) + "s") % "   |  ")
    print (("%" + str(n) + "s%i") % ("   +--", value))
def display (lst, value):#Draws an ASCIT art arrow shwing where
    #the given value is withng the list. lst is list value is the element to locate
    show(lst)
    position = binary_search(lst, value)
    if position != None:
        position = 4 * position + 7;
        draw_arrow(value, position)
    else:
        print ("(", value, "not in list)", sep='')
        print ()
def main ():
    a = [2, 5, 11, 13, 44, 80, 100, 110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)
main()


