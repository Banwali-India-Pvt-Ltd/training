#python filter
l = [1, 2, 3, 4, 5, 6, 7]
#seleect even numnebers
#filte(function, seques


def is_odd(x):
    return x % 2 != 0
P = filter(is_odd, l)
print (list(P))