from math import sqrt
# is_prime(n)
# Determines the primality of a given value
# n an integer to test for primality
# Returns true if n is prime' otherwise, returns false
def is_prime(n):
    result = True   # Provisionally from 2 to the square root of n
    root = sqrt(n)
    trial_factor = 2
    while result and trial_factor <= root:
        result = (n % trial_factor != 0 )    # Is it a factore?
        trial_factor += 1                    # Try next candidtate
    return result
# main
# Tests for primality each integer from 2
# up to a value provided by the user.
# If an integer is prime, it prints it;s
# otherwise, the number is not printed.
def main():
    max_value = int(input("Display primes up to what value? "))
    for value in range(2, max_value + 1):
        if is_prime(value):      # See if value is prime
            print(value, " ")    # Display the prime number
            print()   # Move cursor down to next line
main()        # Run the program