from math import  fabs
def equals(a, b, tolerance):
    return a == b or fabs(a - b) < tolerance;
def main():
    i = 0.0
    while not equals(i, 1.0, 0.0001):
        print("i =", i)
        i += 0.1
main()


