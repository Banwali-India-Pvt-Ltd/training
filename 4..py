# About Function

# return the greatest of three numbers
def get_greatest(a,b,c):
    greatest = -1
    if a > b:
        if a > c:
            greatest = a
        else:
            greatest =c
    elif b > c:
        greatest = b
    else:
        greatest = c
    return greatest

x = 10
y = 20
z = 30

g =  get_greatest(x,y,z)   # g is the greatest of x, y, z
print(g,'is greatest')     # Print greatest value