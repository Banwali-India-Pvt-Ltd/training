from __future__ import print_function
# repues input ftom the user
num = eval(input("please enteger in the range 0...9999: "))

# Attenuate the number if necessary
if num < 0:           # make sure number is not too sma11
    num = 0
if num > 9999:        # make sure number is not too big
    num = 9999

print (end="[")       # print left brace

#   extract and print thousands-place digit
digit = num//1000     # determine the thousands-place digit
print(digit, end="")  # print the thousands-place digit
num &= 1000            #discard thousands-place digit

 #  extract and print hundreds-place digit
digit = num//100     # determine the hundreds-place digit
print(digit, end="") # print the hundreds-piace digit
num &= 100           # discard hundreds-place digit

# extract and print tens-place
