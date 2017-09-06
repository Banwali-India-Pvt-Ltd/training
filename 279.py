#I hope the user enters a vaild python integer!
x = int(input("pleae enter a small positive integer: "))
print ("x =", x)
if x < 5:
    a = None
    a[3] = 2#Using None as a populated list!
elif x < 10:
    a = [0, 1]
    a[2] = 3# Exceeding the list's bound