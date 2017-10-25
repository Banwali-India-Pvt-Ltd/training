from __future__ import  print_function
print("My question no.(1)")
print("Question.  Take two integer numbers and find Area of Rectangle... ")

def Area_Of_Rectangle():   # Define a functon
    num = int(input(" Enter Rectangle Hight... "))    # Take an integer value
    num1 = int(input("Enter Rectangle width... "))    # Take again an integer value
    print("Your Rectangle Hight %s and Width %s ." % (num, num1))
    print("Your answer....")
    print("Area of Rectangle", num * num1)  # Last print this line result
Area_Of_Rectangle()  # Call  the function
print("\n")

print("My question no.(2)")
print("Question. Take tow integer numbers and find Are of Triangle...")
def Area_Of_Triangle():    # Define a function
    num = int(input("Enter Triangle base..."))         # Take an integer value
    num1 = int(input("Enter Trianlge hight..."))       # Take again an integer value
    print("Your Trianlge base %s and hight %s ." %( num, num1))
    print("Your answer....")
    print("Are of Trianlge ", int(num * num1/2))       # Last print this line result
Area_Of_Triangle()  # Call the function
print("\n")

print("My question no.(3)")
print("Question. Take an integer numbber and get the Square...")
def Area_of_Square():
    num = int(input("Enter an integer... "))           # Take an integer value
    print("Your answer..")
    a = (num ** 2)           # Last time print this line
    print("Your %s number square %s ." % (num, a))
Area_of_Square()  # Call the function
print("\n")

print("My question no.(4)")
print("Question. Take an integer number an get cube...? ")
def cube():
    num = int(input("Enter an integer... "))           # Take an integer  value
    a = (int(num ** (1./3.))) # Find cube num value  
    print("Your answer...")
    print("Your number %s cube is %s " % (num, a))
cube() # Call the function
print("\n")

print("My question no.(5)")
print("Qestion. Take an integer number and get Fibonacci number of number...")
def Fibonacci():
    number = int(input("Enter an integer... "))       # Take an integer value
    x = 0                       # Define a variable
    y = 1                       # Define second variable
    count = 0                   # Define third variable
    while count < number:       # Loop running until count value less than number value 
        print(x)                # Print x value
        z = x + y               # Define a new variable z and store x, y value addition
        x = y                   # Change x value
        y = z                   # Change y value
        count += 1              # Count value growth each time 
Fibonacci()  # Call the function

print ("My question no.(6)")
print ("Take two integer and get those prime number in between them")
def is_prime():
    lower = int(input("Enter an integer..."))               # Take an integer value
    upper = int(input("Enter another an integer..."))        # Take again an integer value
    for i in range(lower, upper + 1):   # Loop running
        for j in range(2, i):
            if (i % j) == 0:
                break
            else:
                print(i)
is_prime()  # Call the function

print ("My question no.(7)")
def slicing(a):
    x = int(input("Enter your starting point for slicing... "))       # Take an integer number  
    y = int(input("Enter you end point for slicing... "))             # Take again an integer number
    print(a[x:y])                     # This line print slicing your string
s = input("Enter your stirng... ")
slicing(s)  # Call the function

print ("My question no.(8)")
def Print_first_Character():
    a = input("Enter your string... ")     # Take a string
    print(a[0])                            # Print your string first character
Print_first_Character()  # Call the function

print ("My question no.(9)")
from math import sqrt
def Square_root(x):
    print(int(sqrt(x)))      # Get x value square root
y = int(input("Enter your value... "))       # Take an integer
Square_root(y)  # Call the function

print ("My question no.(10)")
def String_Concatenation(x, y):
    print(x + y)                      # Choose two string done concatenation
a  = input("Enter your string... ")   # Take a string
b = input("Enter your second string... ")    # Take again a string
String_Concatenation(a, b)  # Call the function

print ("My question no.(11)")
def String_Repetition(a):
    print(a * 2)       # print a value second time
x = input("Enter your string... ")  # Take a string
String_Repetition(x)  # Call the function

print ("My question no.(12)")
def Exploring_Data_Types(x):
    y = type(x)
    if y is int:
        print("This input is of type integer. ")  # If x value data type integer than print this line.
    elif y is float:
        print("This input is of type float. ")    # If x value data type float than print this line.
    elif y is str:
        print("This input is of type string. ")   # If x value data type string than pirnt this line.
    else:
        print("This is something else. ")         # If x vlaue data type something than print this line.
a = 2
Exploring_Data_Types(a)  # Call the function

print("My question no.(13)")
def Abs(a):
    print(abs(a)) 
x = int(input("Enter number... "))
Abs(x)  # Call the function

print ("My question no.(14)")
import math
def Ceil(a, b, c, d):
    print(math.ceil(a))
    print(math.ceil(b))
    print(math.ceil(c))
    print(math.ceil(d))
w = int(input("Enter a nagative integer number... "))
x = int(input("Enter a positive integer number... "))
y = float(input("Enter a nagative float number... "))
z = float(input("Enter a positive float number... "))
Ceil(w, x, y, z)

print ("My question no.(15)")
print("About cmp function")
print("If x < y than function returns , -1")
print("If x == y than function returns , 0")
print("If x > y than function returns , 1")
def cmp_to_symbol(val, other_val):
    '''returns the symbol representing the relationship between two values'''
    return [(val > other_val) - (val < other_val)]
x = input("Enter an integer number... ")
y = input("Enter again an integer number... ")
print(cmp_to_symbol(x, y))

import math
print ("My question no.(16)")
def Floor(a, b, c, d):     
    print(math.floor(a))
    print(math.floor(b))
    print(math.floor(c))
    print(math.floor(d))
w = int(input("Enter an nagative integer number... "))   # Take in nagative an integer number
x = int(input("Enter and positive integer number... "))  # Take in positive an integer number 
y = float(input("Enter a nagative float number... "))    # Take in nagative a float number
z = float(input("Enter a positive float number... "))    # Take in positive a float number
Floor(w, x, y, z)  # Call the function

print ("My question no.(17)")
def Min(a, b, c):
    print("Here is minimun number in three number.. ",min(a, b, c))    # Print minimum number
    print("Here is maximum number in three number.. ",max(a, b, c))    # Print maximum number
x = int(input("Enter an integer number... "))       # Take an integer number
y = int(input("Enter again an integer number... ")) # Take again an integer number
z = int(input("Enter again an integer number... ")) # Take again an integer number
Min(x, y, z) # Call the function

print ("My question no.(18)")
def Stirng_Join(a):
    print(" ".join(a))   #
x = "Sukhpal","Choudhary","Banwal"
Stirng_Join(x)     # Call the function

print("My question no.(19)")
def Lower(a):
    print(a.lower())      # Print lower position string
x = "THIS IS TECHGIG"     # Take upper position stirng
Lower(x)  # Call the function

print ("My question no.(20)")
def Is_lower(x):
    print(x.islower())     # If x value stirng is lower than print 'True' else: print 'False'
x = "this"      # Take a string in lower position
Is_lower(x)  # Call the function

print ("My question no.(21)")
def Is_numeric(a):
    print(a.isnumeric())       # If a value is numeric than print 'True' else print 'False'
x = u"Next year is 2018"          # Take a numeric
Is_numeric(x)  # Call the function

print ("My question no.(22)")
def Is_title(y):
    print(y.istitle())   #  If stirng is title pring 'True' else: print 'False'
x = "This Is String Example"   # Take title position strin
Is_title(x)  # Call the main function and Run the program

print ("My question no.(23)")
def Is_upper(x):
    print(x.isupper())         # If string is upper than print True, else: print 'False'
x = "THIS IS TECHGIG"          # Take a string upper position
Is_upper(x)  # Call the function

print ("My question no.(24)")
def String_len(x):
    print(len(x))      # Print string length
y = str(input("Enter your string... "))         # Take a stirng by users
String_len(y)  # Call the function

print ("My question no.(25)")
def Lstrip(a):
    print(a.lstrip())  # Delet the space and print "This is Techgig"
x = "    This is Techgig"
Lstrip(x)  # Call the main function and Run the program

print ("My question no.(26)")
def String_max(x):
    print(max(x))  # Print y
y = str(input("Enter your stirng... "))
String_max(y)  # Call the main function and Run the Program

print ("My question no.(27)")
def String_min(x):
    print(min(x))      # Print minimum alphabet 
y = str(input("Enter your string... "))           # Take a string by users
String_min(y)  # Call the function

''' This cod find prime numbers lying
    between the given range.
    and Output will be the single number
    which tell how many prime numbers are
    there between given range.'''
print ("My question no.(28)")
def main():
    num = int(input("Enter an integer number ? "))          # Take an integer number
    val = int(input("Enter another an integer number ?"))   # Take again an integer number
    count = []                 # Define a empty
    for i in range(num, val):  # Loop running 18 times
        if i > 1:
            for j in range(2, i):      # Loop running 2 between i value ( eg. (2, 4)  loop running 2 times)
                if i % j == 0:
                    break
            else:
                a = (count.append(i))  # Here this line append i value primes number and return count
    print(len(count))                  # Than after print length of count = 7

main()          # Call the main function

''' This code first time take as some number
    after number // 10 each time change number
    value and print loop time (5)'''
print ("My question no.(28)")
def Num_len():
    number = int(input("Enter your number"))    # Take an integer number
    count = 0
    while number:           # Loop running while number
        count += 1
        number //= 10       # this line divide by 10 or number value change each time
    print(count)            # Than after print count value 5

Num_len()  # Call the main function

print ("My question no.(29)")
def Armstrong():
    num = int(input("Enter a number "))    # Get a number
    Sum = 0
    temp = num         # Store num value
    while temp > 0:    # Loop till the quotient is 0
        digit = temp % 10   # Find Reminder
        Sum += digit ** 3   # Cube reminder and add it to the Sum
        temp //= 10
    # If the entered number and the Sum  value matches, it is an Armstrong numbers
    if num == Sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
Armstrong() # Call the function

print ("My question no.(30)")
def Factorial():
    count = 1         # Define a variable
    num = 1           # Define again variable
    factorial = int(input("Enter your factorial number:.. "))        # Choose your factorial 1,2,3.....
    while num <=  factorial:           # Loop running while num value less than factorial value
        count *= num  # Multiple count and num value
        num += 1      # num value growth each time
    print(count)      # Last time print count value
Factorial()  # Call the function

# This code Find second largest number
print ("My question no.(31)")
def Second_Largest():
    lst = [11, 55, 44, 22, 33 ]
    lst.sort()       # This line sorted last value
    print(lst[-2])   # Find second largest number in lst
Second_Largest()  # Call the main function

print ("My question no.(32)")
def power(base,exp):
    if(exp == 1):
        return (base)     # If exp value 1 return only base value
    if (exp != 1):
        return (base*power(base, exp - 1))       # Return base exponential value
base = int(input("Enter base: "))                # Take an integer number for base 
exp = int(input("Enter exponential value: "))    # Take again an integer number for exponential value
print("Result: ",power(base,exp))  # Call the function

''' This code count upper and lower letters'''
print ("My question no.(33)")
def Count_letters():
    string = input("Enter your string ? -> ")     # Take a string
    count1 = 0
    count2 = 0
    for i in string:             # Loop running string length defend
        if (i.isupper()):
            count1 = count1 + 1  # If string is upper than count + 1
        elif (i.islower()):
            count2 = count2 + 1  # If string is lower than count + 1
    print("This stirng in %s Capital letters" % count1)   # Print count1 value
    print("This stirng in %s Small letters" % count2)     # Print count2 value
Count_letters()  # Call the main function

# Program to add two matrices using nested loops
print ("My question no.(34)")
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Iterate through rows
for i in range(len(X)):
    # Iterate through columns
    for j in range(len(X[0])):
        result[i] [j] = X[i] [j] + Y [i] [j]
for r in result:
    print(r)
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0,  0, 0]]


# Iterate through rows
for i in range(len(X)):
    # Iterate through columns
    for j in range(len(X[0])):
        result[i] [j] = X[i] [j]
for r in result:
    print(r)

# This code find greatest divisior  in two integer values.
print ("My question no.(35)")
def gcd(a, b):
    if(b == 0):
        return a             # As the result of B is 0,                             # The value of A will be printed.
    else:
        return gcd(b, a%b)   # As long as the result of B is greater than 0,                             # The function call will be called
a = int(input("Enter first number? "))     # Take an integer number
b = int(input("Enter second number? "))    # Take another an integer number
GCD = gcd(a, b)      # Call the main function
print("GCD is: ")    # Print this line
print(GCD)

print ("My question no.(36)")
def computeHCF(x, y):
     # If x value greater than y so will smaller y,
     # If x value less than y so will smaller x
    if x > y:          
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):          # Loop running 1 to smaller value + 1 times
        if (((x % i == 0) and y % i == 0)):  # If condition True than check next line
            hcf = i
    return hcf      # Last Return hcf(i),  print i value
num1 = int(input("Enter an ineger number... "))    # Take an integer number
num2 = int(input("Enter an integer number.. "))    # Take again an integer number
print(computeHCF(num1, num2))  # Call the function

print ("My question no.(37)")
def Sorted_Dict():
    mydict = {'fortran': 40, 'java': 2, 'perl':1, 'python':3, 'php': 5, 'javascript':6, 'c':7, 'cpp': 8, 'ruby':9, 'csharp':10}
    print("Sort by keys: ")
    for x in sorted(mydict.keys()):
        print(x)
Sorted_Dict()

#  This code search  the greatest factorial number of two integers
print ("My question no.(38)")
def GCF(num1, num2):
    for x in range(num1, 0, -1):           # Loop running 18 times in reverse position

        ''' Yet num1 value% x == 0 and num2 value% x == 0
        So the value of x will be printed.'''

        if num1 % x == 0 and num2 % x == 0:
            return x       # X value ( will be printed 6 )


num1 = int(input("Enter an integer number(Factorial) ... "))
num2 = int(input("Enter an integer number(Factorial) ... "))
print(GCF(num1, num2))  # Call the gcf function

print ("My question no.(39)")
import array
def Create_array():
    arr = array.array('i', [1, 2, 3])             # Define a array in list
    print("The new created array is: ", end="")   
    for i in range(0,3):         # Loop running 3 times
        print(arr[i], end=" ")   # Print different value each time of array
Create_array()  # Call the function

print ("My question no.(40)")
def Append_array():
    arr = array.array('i', [1, 2, 3])        # Define a array
    arr.append(4)           # Append a element in array
    print("The append array is: ", end="")
    for i in range(0, 4):     # Loop running 4 times
        print(arr[i], end=" ")        # different value each times of array
Append_array()  # Call the function

print ("My question no.(41)")
def Insert_array():
    arr = array.array('i', [1,3,4,5])     # Define a array
    arr.insert(1,2)     # insert 2 number in array
    print("The insert array is: ", end="")   
    for i in range(0, 5):         # Loop running 5 times
        print(arr[i], end=" ")    # Print different value each time of arr

Insert_array()  # Call the function

print ("My question no.(42)")
def Check_element_place():
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])    # Define a array
    print("The check element place array is: ", end="")    # Print this line
    print(arr.index(3))      # Check 3 element in array
Check_element_place()  # Call the function

print ("My question no.(43)")
def Check_element_place():
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])     # define a array
    arr.reverse()       # Array reverse
    print("The reverse array is: ", end="")     # Print this line
    for i in range(0, 9):        # Loop running 9 times
        print(arr[i], end=" ")   # Print different value each time of arr
Check_element_place()  # Call the function

print ("My question no.(44)")
def Pop_element():
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])   # Define a array
    arr.pop(3)           # Pop e number element in array 
    print("The pop array is: ", end="")     # Print this line
    for i in range(0, 8):        # Loop running 8 times
        print(arr[i], end=" ")   # Print different value each times of arr 
Pop_element()  # Call the function

print ("My question no.(45)")
def Remove():
    arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])  # Define a array
    arr.remove(8)            # Remove number 8 in array
    print("The remove array is: ", end="")   # Print this line
    for i in range(0, 8):              # Loop running 8 times
        print(arr[i], end=" ")         # Print different value each time of arr 
Remove()  # Call the function

# Python program to find if there are two elements wtih given sum
CONST_MAX = 10000000
print ("My question no.(46)")
# function to check for the given sum in the array
def Find_Pairs(arr, arr_size, sum):
    # initialize hash map as 0
    binmap = [0] * CONST_MAX
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and binmap[temp] == 1):
            print ("Pair with the given sum is", arr[i], "and", temp)
        binmap[arr[i]] = 1
# driver program to check the above function
A = [1, 4, 45, 6, 10, -8]
n = 16
Find_Pairs(A, len(A), n)

print ("My question no.(47)")
# Count Element in array
def count_element():
    arr = array.array('i', [1,2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
    print(arr.count(5))
count_element()

print ("My question no.(48)")
def array_extend():
    arr = array.array('i', [1,2, 3, 4, 5, 6])
    arr1 = array.array('i', [7, 8, 9])
    arr.extend(arr1)
    print("The modifiend array is :", end="")
    for i in range(0, 9):
        print(arr[i], end=" ")
array_extend()

print ("My question no.(49)")
def array_fromlist():
    arr = array.array('i',[1, 2, 3, 4,])
    arr2 = [5, 6, 7, 8]
    arr.fromlist(arr2)
    print("The modified array is :", end="")
    for i in range(0, 8):
        print(arr[i], end=" ")
array_fromlist()

print ("My question no.(50)")
def array_tolist():
    arr = array.array('i',[1, 2, 3, 4,])
    arr2 = arr.tolist()
    print(arr2)
    print("The new list created is :", end="")
    for i in range(0, len(arr2)):
        print(arr2[i], end=" ")
array_tolist()

print ("My question no.(51)")
def array_typecode():
    arr = array.array('i',[1,2,4,5])
    print("The datatype of array is :->", end=" ")
    print(arr.typecode)
array_typecode()

print ("My question no.(52)")
def Majority_element(lst):
   idx, ctr = 0, 1
   for i in range(1, len(lst)):
       if lst[idx] == lst[i]:
           ctr += 1

       else:
           ctr -= 1
           if ctr == 0:
               idx = i
               ctr = 1

       return lst[idx]
lst = [1, 2, 1, 2, 3, 4, 4, 5, 3]
print(Majority_element(lst))

print ("My question no.(53)")
# This code Multiplication between even and odd value
def list(a, b):         # Define a list function
    even = 0            # Define a variable
    odd = 0             # Define second variable
    for i in range(b):  # Loop running 5 time
        if i % 2 == 0:
            even += a[i]     # If i value % 2 == 0: than store even += a[i] value
        else:
            odd += a[i]      # If i value % 2 != 0: than store odd += a[i] value

    print(even * odd)        # And last print even value * odd value = 54
x = [1, 2, 3, 4, 5]     # Make a list
y = len(x)              # Find the lenght of x list
list(x, y)  # Call the list function

print ("My question no.(54)")
def average(somn):
    tot = 0
    for i in somn:
        tot = tot+i
    zavg = tot/len(somn)
    return zavg
lst = [1, 2, 3, 4, 5]
print(average(lst))

print ("My question no.(55)")
def String_position(search, target):
    first = (search.find(target))  # Check
    return (search.find(target,first+1))
hobby = ("I like to play guitar and i am learning guitar")    #
print (String_position(hobby,"guitar"))  # Run the program start and call position2 function
a = ("Hey! I play cricket and i want to learn cricket very well in few days")
x = (a.find("cricket"))
y = (a.find("cricket", x  +1))
print (y)
print (a[y:])

