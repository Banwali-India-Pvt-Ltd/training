from __future__ import  print_function
#tree (height)
#Draws a tree of a given height
#height is the height of the displayed tree
def tree (height):
    row = 0
    while row < height:       #first row, from the top, to draw
        #print leading spaces
        count = 0
        while count < height - row:
            print (end=" ")
            count += 1
#print out stars, twice, the current row plus one:
#1. number of stars on left side of tree
#=current row value
#2. exactly one star in the center of tree
#3. number of stars on right side of tree
    count = 0
    while count < 2*row + 1:
        print (end="*")
        count += 1
        #move cursor to next line
    print ()
    row += 1
    #main
    #Allows users to drow of various
def main ():
    height = int(input("Enter height of tree:"))
    tree(height)
main ()

