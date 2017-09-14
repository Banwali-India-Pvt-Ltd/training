# The program related to if statement
# first request user to give inputs
from __future__ import print_function
num = eval(raw_input('Please enter an integer in the range 0...9999:'))

# Attenuate the number if necessary
if num < 0:
    num = 0

if num > 9999:
    num = 9999

print(end="[")     # print left brace

# Extract and print thousands-place digit
digit = num//1000    # Determine the thousands-place digit
print(digit, end="")  # print the thousands-place digit
num %= 1000

# Extract and print hundred-place digit
digit = num//100  # determine the hundreds-place digit
print(digit, end="")  # print the hundreds-place digit
num %= 100             # discard tens-place digit

# Extract and print tens-place digit
digit = num//10    # determine the ten-place digit
print(digit, end="")   # print the tens-place digit

# Remainder is the one-place digit
print(num, end="")  # Print the one-place digit
print("]")          # print right brace

