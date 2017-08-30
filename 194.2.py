# Chapter 9
# 9.2 List Assignment and Equivalence

def list_copy(lst):
    result = []
    for item in lst:
        result += [item]
    return result

def main():
    a = [10, 20, 30, 40]     # a and b are distinct lists that contain the same elements
    b = list_copy(a)          # Make a copy of a
    print('a =', a, ' b =', b)

    print('Is ',a, ' equal to ', b, '?')
    print(a == b)

    print('Are ', a, ' and ', b, ' aliases?')
    print(a is b)

    b[2] = 35       # Change an element of b
    print('a =', a, ' b =', b)
main()