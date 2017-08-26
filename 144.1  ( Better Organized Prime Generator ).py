# Chapter 7 ( Writing Functions )
# Page No. 144.1 , 7.5.1 - Better Organized Prime Generator


from math import sqrt
def is_prime(n):     # is_prime (n) # Determines the primality of a given value
                    #  n an integer to test for primality #   Returns true if n is prime; otherwise, returns false
    result = True     # Provisionally, n is prime
    root = sqrt(n)
    trial_factor = 2     # Try all potential factors from 2 to the square root n
    while result and trial_factor <= root:
        result = (n % trial_factor != 0 )     # Is it a factor?
        trial_factor += 1     # Try next candidate
        return result
def main():     # main # Tests for primality each integer from 2 # up to a value provided by the user.
                #  If an integer is prime, it prints it; # otherwise, the number is not printed.

    max_value = int(input("Dispaly primes up to what value? "))
    for value in range (2, max_value + 1):
        if is_prime(value):     # See if value is prime
            print(value)     # Display the prime number
    print()     # Move cursor down to next line
main()     # Run the program
