# About Function

# Print the greatest of three numbers
def print_greatest(a,b,c):
    if a > b:
        if b > a:
            print(b, 'is greatest')
        else:
            print(a, 'is greatest')
    elif b > c:
        print(b, 'is greatest')
    else:
        print(c, 'is greatest')

x = 12
y = 15
z = 20

print_greatest(x,y,z)    # Print the greatest value