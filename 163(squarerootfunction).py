def square_root(val):
    root = 1.0
    diff = root*root -val
    while diff > 0.00000001 or diff < -0.00000001:
        root =(root + val/root) / 2
        diff = root*root - val
    return root
def main():
    num = float(input("enter number: "))
    print("square root of", num, "=", square_root(num))
main()