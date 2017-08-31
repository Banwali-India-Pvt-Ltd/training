# Chapter 9
# 9.6 Prime Generation with a List

# Display the prime numbers between 2 and 500
# Largest potential prime considered

MAX = 500
def main():
            # Each position in the Boolean list indicates
            # if the number of that position is not prime:
            # false means " prime, " and true mens "composite."
            # Initially all numbers are prime until proven otherwise
    nonprimes = MAX * [False]     # Initialize to all False
    nonprimes[0] = nonprimes[1] = True       # First prime number is 2; 0 and 1 are not prime
    for i in range(2, MAX + 1):       # Start at the first prime number, 2.
        if not nonprimes[i]:          # See if i is prime
            print(i)
            for j in range(2*i, MAX + 1, i):
                nonprimes[j] = True   # It is prime, so eliminate all of its
                                      # multiples that cannot be prime
    print()               # Move cursor down to next line

main()