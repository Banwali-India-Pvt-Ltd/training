from __future__ import  print_function
max_value = eval(input('display primes up to what value? '))
for value in range(2, max_value + 1):
    is_prime = True
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False
            break
    if is_prime:
        print(value, end=' ')
print()

