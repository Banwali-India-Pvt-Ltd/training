from __future__ import  print_function
def list_copy (lst):
    result = []
    for item in lst:
        result += [item]
        return result
def main():
    #a and b are distinct lists that contain the same elsa
    a = [10, 20, 30, 40]
    b = list_copy(a)
    print ('a =', a,' b =', b)
    print ('Is ', a, 'equal to ', b, '?', sep='', end=' ')
    print (a == b)
    print ('Are ', a, 'and', b, 'aliases?', sep='', end=' ')
    print (a is b)
    b[2] = 35
    print ('a =', a,'  b=', b)
main()