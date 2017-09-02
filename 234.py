#use the standard permutations
#the possible arrangements of elements in list.
from itertools import permutations
def main():
    a = [1, 2, 3, 4]
    for p in permutations(a):
        print(p)
main()
