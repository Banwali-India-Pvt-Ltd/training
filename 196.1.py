# Chapter 9
# 9.3 List Bounds

# Make a list containing 100 zeros
v = [0] * 100
x = int(input("Enter an integer: "))     # User enters x at run time
if 0 <= x < len(v):     # Ensure index is within list bounds
    v[x] = 1     # This should be fine
else:
    print("Value provided is out of range")
