from __future__ import  print_function
def locate(lst, seek):
    '''
    Returns the index of elements seek in list lst,
    if seek is present in lst.
    Returns None if seek is not an element of lst.
    lst is the lst in which to search
    seek is the element to find.
    '''
    for i in range(len(lst)):
        if lst[i] == seek:
            return i       # Return position immediately
    return None            # Element not found

def format(i):
    '''
    Prints integer i right justified in a 4-space
    field.  Prints "****" if i > 9,999.
    '''
    if i > 9999:
        print("****")        # Too big!
    else:
        print("%4d" % i)

def show(lst):
    '''
    Prints the contents of list lst
    '''
    for item in lst:
        print("%4d" % item, end='')   # Print element right justifies in 4 spaces
    print()                           # Print newline

def draw_arrow(value, n):
    '''
    Print an arrow to value which is an element in a list.
    n specifies the horizontal offset of the arrow.
    '''
    print(("%" + str(n) + "s") % "   ^   ")
    print(("%" + str(n) + "s") % "   |   ")
    print(("%" + str(n) + "s%i") % ("   +-- ", value))


def display(lst, value):
    '''
    Draws an ASCII art arrow showing where
    the given value is within the list.
    lst is the list.
    value is the element to locate.
    '''
    show(lst)                    # Print contents of the list
    position = locate(lst, value)
    if position != None:
        position = 4*position + 7;         # Compute spacing for arrow
        draw_arrow(value, position)
    else:
        print("(", value, " not in list)", sep='')
    print()


def main():
    a = [100, 44, 2, 80, 5, 13, 11, 2, 110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)

main()