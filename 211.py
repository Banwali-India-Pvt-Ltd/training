#count the number of prime numbers lees thrn
#2 million and timen how long it taken
#compares the performance of two different
#algorithms.
from time import clock
from  math import sqrt
def count_prime (n):
    start = clock()#record start time
    count = 0
    for val in range(2,n):
        result = True  #Provionally, n is the square root of n
        root = int (sqrt(val) + 1)
        #Try all potential factors from 2 to the squre root of n
        trial_factor = 2
        while result and trial_factor <= root:
            result = (val%trial_factor !=0)     #is it a factor
            trial_factor += 1                   #try next candidate
            if result :
                count +=1
        stop = clock ()  #stop the clock
        print ("count =", count, "Elapsed time:", stop - start, "seconds")
def seive (n):
              #generates all the prime from numbers from 2 to n -1
#n-1 is the largest potential prime considered
    start = clock()
    nonprimes = n*[False]
    count = 0
    nonprimes[0] = nonprimes[1] = True
    for i in range(2,n):
        #see if i prime
        if not nonprimes[i]:
            count +=1
            for j in range(2*i, n, i):
                nonprimes[j]
    stop = clock()
    print ("count =", count, "Elapsed time:", stop -start, "seconds")
def main():
    count_prime(2000000)
    seive (2000000)
main()