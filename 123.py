from __future__ import print_function
from time import clock

print("Enter your name: ", end="")
start_time = clock()
name = raw_input()
elapsed = clock() - start_time
print(name, "it took you", elapsed, "seconds to respond")