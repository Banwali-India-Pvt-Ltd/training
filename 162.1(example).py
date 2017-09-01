def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        a = b
        b = a+b
        print(a,'this is fibo num')
    return b
num = int(input("enter the value of n: "))
print(fibo(num))
