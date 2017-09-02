from __future__ import   print_function
#  LINEARSEARCH.PY
def locate(lst,seek):               #returns the index of element seek in list lst,
               #if seek is present in lst.
               #Returns nons if seek is not an element of lst.
    for i in range(len(lst)):
        if lst[i] == seek:
            return i#Return positin immdistely
        return None#element not found
def format(i):
    #print integer i rigrer justified in a 4-space
    if i > 9999:
        print ("***")   #Too big!
    else:
        print ("%4d" % i)
def show (lst):
    for item in lst:  #printe integer i right justified in a 4-sqace
        print ("%4d" % item, end='')#field print "***" if i >9,999.
    print ()
def draw_arrow (value, n):
    print (("%" + str(n) + "s") % "  ^  ")
    print (("%" + str(n) + "s") % "  |  ")
    print (("%" + str(n) + "s%i") % (" +--", value))
def display (lst, value):
    show(lst) #Draws an ASCII art arrow showing where
    #the give value is within the list lst is the list value is to locate
    position = locate(lst, value)
    if position != None:
        position = 4*position + 7; #print element right justifies in 4 sppaces
        draw_arrow(value,position) #print new line
    else:
        print ()
def main():
    a = [100, 44, 2, 80, 5, 13, 11, 2, 110]
    display(a, 13)
    display(a,  2)
    display(a,  7)
    display(a, 100)
    display(a, 110)
main()
