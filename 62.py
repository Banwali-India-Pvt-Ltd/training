import os
d = os.getcwd()
print (d)




import os
d = os.getcwd()
#python string\abcd ------windows
#python -vstring/abcd------linux/unix
d1 = os.path.join(d, "abed")
fname = os.path.join(d1, "a.txt")
print (fname)
f = open(fname, "r")

for l in f:
    print (l)