from __future__ import  print_function
def gcd(m, n):
    min = m if m < n else n
    largestFactor = 1
    for i in range(1, min + 1):
        if m % i == 0 and n % i == 0:
            largestFactor = i
    return largestFactor
def get_int():
    return int(input("please enter an integer: "))
def main():
    n1 = get_int()
    n2 = get_int()
    print("gcd(", n1, ",", n2, ") = ", gcd(n1, n2), sep="")
main()
