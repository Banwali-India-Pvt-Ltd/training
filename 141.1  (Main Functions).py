# Chapter -7 Using Functions
# Page N. 141.1

# Computes the greatest common divisor of m and n
def gcd(m, n):
    min = m if m < n else n     # Determine the smaller of m and n
    largestFactor = 1     # 1 is definitely a common factor to all ints
    for i in range(1, min + 1):
        if m % i == 0 and n % i == 0:
            largestFactor = i     # Found larger factor
    return largestFactor
def get_int():     # Get an integer from the user
    return int(input("Please enter an integer: "))
def main():     # Main code to execute
    n1 = get_int()       
    n2 = get_int()
    print("gcd(", n1, ",", n2, ") = ", gcd(n1, n2))

main()     # Run  the program
