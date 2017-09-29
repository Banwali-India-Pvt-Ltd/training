def func():
    i = 0
    while (i < 10):
            j = i*i
            if j < 50:
                i = i+1
                continue
            print ('square:',j)
            i = i+1
func()