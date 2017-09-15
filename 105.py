# The program returns prime number via while loop
# The proram doesn't return any value
from __future__ import print_function

max_value = eval(raw_input('Display primes up to what value?'))
value = 2   # Smallest prime number
while value <= max_value:
    # See if value is prime
    is_prime = True   # Provisionally, value is prime
    # Try all possible factors from 2 to value - 1

    trial_factor = 2
while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False;   # Found a factor
            break         # No need to continue; it is NOT prime
        trial_factor += 1  # Try the next potential factor
if is_prime:
        print(value, end= ' ')  # display the prime number
        value += 1            # Try the next potential prime number
print()                       # Move cursor down to next line