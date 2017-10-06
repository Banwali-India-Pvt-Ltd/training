for i in range(5):
    print i
    if i%2==0:           # we aren't interested in the even numbers, skip those
        print "even"
        continue
    else:
        print "odd"
    print "calculating"
    iSum = iSum + i
    iProduct = iProduct * i

print "========="
print iSum
print iProduct