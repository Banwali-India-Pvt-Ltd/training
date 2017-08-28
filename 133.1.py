
from math import  sqrt
from  time import  clock
max_value = 10000
count = 0
value = 2
start = clock()
while value <= max_value:
    is_prime = True
    trial_factor = 2
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False;
            break
        trial_factor += 1
    if is_prime:
            count += 1
    value += 1
elapesd = clock() - start
print("count:", count, " elapesd time:", elapesd, "sec")


