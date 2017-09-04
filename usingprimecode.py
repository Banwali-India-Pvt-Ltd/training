from primecode import is_prime

def mian():

    num = int(input("Enter an enteger: "))
    if  is_prime(num):
        print(num, "is prime")
    else:
        print(num, "is NOT prime")
print is_prime(4)