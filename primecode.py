# Contains the definition of the is_prime function
from math import sqrt

#  Returns True if non_negative integer n is prime;
#  otherwise, returns false
def is_prime(n):
    trial_factor = 2
    root = sqrt(n)

    while trial_factor <= root:
        if n % trial_factor == 0:   # Is trialFactor a factor?
            return False;          # Yes, return right away

    return True;                   # Tried them all, must be prime