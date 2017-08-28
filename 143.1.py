#file simplefunction.py
from __future__ import print_function
def prompt():
    print ("please enter an value:", end=" ")
  #start of progrprint
print ("this program adds together two integers.")
prompt()   #call the function
value1 = int (input ())
prompt() #call the function again
value2 = int (input())
sum = value1 + value2
print (value1, "+", value2,"=", sum)
