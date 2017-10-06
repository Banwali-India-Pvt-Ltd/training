for i in range(2, 10):
        for x in range(2, i):
                if i % x == 0:
                        print i, '=', x, '*', i/x
                        break
        else:
        # loop fell through without finding a factor
                print i, 'is a prime number'