# The program prints prime values
from __future__ import print_function
max_value = eval(raw_input('Display primes up to what value?'))
# Try values form 2 (smallest prime number) to max_value

for value in range(2, max_value + 1):
    # See if value is prime
    is_prime = True # Provisionally, value is pirme
           # Try all possible factors from 2 to value -1
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False    #Found a factor
            break    #No need to continue; it not prime
    if is_prime:
        print(value, end= ' ')   # Display the prime number
print()    # Move cursor down to lnext line