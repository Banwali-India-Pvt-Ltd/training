# The program takes value if there is end= operator then
# it will remain in the same line. It doesn't matter the operator
# have before or end of the line
# if we write \n with end operator then it will leave current line


from __future__ import print_function
print ('Please enter an integer value:', end='')
print (end='Please enter an integer value:')
print('Please enter an integer value:')
print('Please enter an integer value:', end='\n')