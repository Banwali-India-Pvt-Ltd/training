a = 0
while a < 100:
    a += 1 # Same as a = a + 1
    print (a)


a = 0
while a < 1000:
    a += 1
    print (a)

    a = 1
    s = 0
    print ('Enter Numbers to add to the sum.')
    print ('Enter 0 to quit.')
    while a != 0:
        print ('Current Sum: ', s)
        a = raw_input('Number? ')
        a = float(a)
        s += a
    print ('Total Sum = ', s)