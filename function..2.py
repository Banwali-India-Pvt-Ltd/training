# return the greatest of three numbers
def get_greatest(a, b, c):
    greatest = 1;
    if a > b:
        if a > c:
            greatest = a
        else:
            greatest = c
    elif b > c:
        greatest = b
    else:
        greatest = c
    return greatest

p = 10
q = 11
r = 12

# g is the greatest of p, q, r
g = get_greatest(p,r,q)
print  g, 'is greatest'