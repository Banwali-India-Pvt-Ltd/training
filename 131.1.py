from math import sqrt
max_value = eval(input('display primes up to what value? '))
value = 2
while value <= max_value:
    is_prime = True
    trial_factor = 2
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
         is_prime = False;
    if is_prime:
        print(value,  ' ')
        value += 1
        print()
