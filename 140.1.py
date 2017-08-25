def gcd(num1, num2):
    min = num1 if num1 < num2 else num2       # Determine the smaller of num1 and num2
    largestFactor = 1                         # 1 is definitely a common factor to all ints
    for i in range(1, min +1):
        if num1 % i == 0 and num2 % i == 0:
            largestFactor = i                 # Fount larger factor
    return largestFactor
print("Pleae enter a integer.")
print("largestFactor")