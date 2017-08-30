from __future__ import  print_function
def main():
    #set up variables
    sum = 0.0
    NUMBER_OF_ENTRIES = 5
    numbers = []
    #Get input from user
    print ("please enter ", NUMBER_OF_ENTRIES,"number:")
    for i in range (0,NUMBER_OF_ENTRIES):
        num = eval(input("Enter number " + str (i) + ":"))
        numbers += [num]
        sum += num;
        #print the numers entered
        print ("end=Numbers entered:")
        for num in numbers:
            print (num, end=" ")
        print ()    #print nowline
        #print  average
        print (" Average:", sum/NUMBER_OF_ENTRIES)
main ()

