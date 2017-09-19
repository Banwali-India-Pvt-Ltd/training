print('!* Python Multiplication Table from 2 to 10\n')
def Multiplication_Table1():
    for i in range(2, 11):
        for j in range(1, 11):
            mul = i * j
            print mul,
        print "\n"

print('!* Multiplication Table from 2 to 10\n')
def Multiplication_Table():
    a = []
    for i in range(2,11):
        for j in range(1, 11):
            mul = i * j
            a.append(mul)
        print(a)
        for k in range(1, 11):
            a.pop()