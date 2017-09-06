# Count th enumber of prime numbers less than
# 2 million and time how long it takes
# Compares the performance of two different
# algorithms

from time import  clock
from  math import  sqrt


def count_primes(n):
    '''
    Generates all the prime numbers from 2 to n - 1.
    n - 1 is the largest potential prime considered.
    '''
    start = clock()     # Record start time

    count = 0
    for val in range(2, n):
        result = True    # Provisionally, n is prime
        root = int(sqrt(val) + 1)
        # Try all potential factors from 2 to the square root of n
        trial_factor = 2
        while result and trial_factor <= root:
            result = (val % trial_factor != 0)   # Is it a factor?
            trial_factor += 1                    # Try next candidate
        if result:
            count += 1

    stop = clock()      # Stop the clock
    print("count =", count, "Elapsed time:", stop - start, "seconds")



def seive(n):
    '''
    Generates all the prime numbers from 2 to n - 1.
    n - 1 is the largest potential prime considered.
    Alogorithm originally developed by Eratosthenes.
    '''

    start = clock()       # Record start time

    # Each position in the boolean list indicates
    # if the number of that position is not prime:
    # false means"prime," and true means "composite."
    # Initially all numbers are prime until proven to all False
    nonprimes = n * [False]    # Global list initialized to all False


    count = 0

    # First prime number is 2; 0 and 1 are not prime
    nonprimes[0] = nonprimes[1] = True

    # Start at the first prime number, 2.
    for i in range(2, n):
        # See if i is prime
        if not nonprimes[i]:
            count += 1
        # It is prime, so eliminate all of its
        # multiples that cannot be prime
        for j in range(2*i, n, i):
               nonprimes[j] = True
    # Print the elapsed time
    stop = clock()
    print("Count =", count, "Elapsed time:", stop - start, "seconds")


def main():
    count_primes(2000000)
    seive(2000000)

main()