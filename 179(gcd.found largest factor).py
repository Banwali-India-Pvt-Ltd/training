def gcd(m, n):
    if n == 0:
        return  m
    else:
        return gcd(n, m % n)
def iterative_gcd(num1, num2):
    min = num1 if num1 < num2 else num2
    largestFactor = 1;
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largestFactor = i
        return largestFactor
def main():
    for num1 in range(1, 101):
        for num2 in range(1, 101):
            print("gcd of", num1, "and", num2, "is", gcd(num1, num2))
main()