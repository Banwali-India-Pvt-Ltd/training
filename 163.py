# Computes the approximate square root of val
# val is an number
def square_root(val):
# Compute a provisional square root
    root = 1.0
# How far off is our provisional root?
    diff = root*root - val#Loop the provisional root
    while diff > 0.00000001 or diff < -0.00000001 :#is close enough to the actual root
        root = (root + val/root)/2#how bad is our current approximation
        diff = root*root - val
    return root
def main():   #get value from the user
    num = float(input("Enter number: "))#report square root
    print ("Square root of", num, "=", square_root(num) )
main ()
