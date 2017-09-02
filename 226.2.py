# Chapter 10
# Randomly Permuting a List


from random import randrange

def permute(lst):
              # Randomly permutes the contents of list lst
    n = len(lst)
    for i in range(n - 1):
        pos = randrange(i, n)       # i <= pos < n
        lst[i], lst[pos] = lst[pos], lst[i]
def main():
         # Tests the function that randomly permutes the contents of a list
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Before:', a)
    permute(a)  # Call the def permute function
    print('After :', a)

main()  # Run the program