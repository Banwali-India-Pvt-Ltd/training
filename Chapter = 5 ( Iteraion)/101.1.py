# Chapter -5 Iteration
# 5.7.1 Computting Square Root

val = eval(input('Enter number: '))
root = 1.0;
diff = root*root - val
while diff > 0.00000001 or diff < -0.000000001:
    root = (root + val/root) / 2
    print(root, 'squared is', root*root)
    diff = root*root - val
