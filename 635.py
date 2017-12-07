def fibonc(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b,a+b

    return output
b = int(input())
print fibonc(b)

def even(n):
    if n%2 == 0:
        print "right"
    else:
        print "wrong"
num = input()
print even(numd)