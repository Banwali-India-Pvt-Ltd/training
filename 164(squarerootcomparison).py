from math import fabs, sqrt
def equals(a, b, tolerance):
    return a == b or fabs(a - b) < tolerance;
def square_root(val):
    root = 1.0;
    diff = root*root - val
    while diff > 0.00000001 or diff < -0.00000001:
        root = (root + val/root) / 2
        diff = root*root - val
    return root
def main():
    d = 0.0
    while d < 100000.0:
        if not equals(square_root(d), sqrt(d), 0.001):
            print(d, ": Expected", sqrt(d), "but computed", square_root(d))
        d += 0.0001
# Here is one issue why no its showing value when I've run it.