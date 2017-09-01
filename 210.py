from __future__ import print_function #display the numbers between
#largest  potentime considered
MAX = 500
def main():     #each position in the boolean list indic
    non_prime = MAX*[False]#if the number of that position is not prime:
    print(non_prime.count(False))#initialize to all False
    non_prime[0] = non_prime[1] = True#first prime is 2; 0are not prime
    for i in range(2, MAX):
        if not non_prime[i]:#seeif i is prime
            print(i, end=" ")
            for j in range(2*i, MAX, i):
                non_prime[j] = True
    print()

if __name__ == '__main__':
    main()

