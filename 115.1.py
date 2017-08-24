from __future__ import print_function
max_value = eval(input('Display primes up to what value? '))
value = 2
while value <= max_value:
    is_prime = True
    trial_factor = 2
    while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False;
            break
        trial_factor += 1
    if is_prime:
        print(value, end=' |')
    value += 1
print()