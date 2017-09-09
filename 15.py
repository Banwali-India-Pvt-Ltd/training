#python continue in while loop
#in while  loop you have to take care of the indution variabale
def func():
    i = 0
    while(i < 10):
        j = i*i
        if j < 50:
            i = i+1
            continue
        print ('square:',j)
        i = i+1
func()



def func():
    i = 0
    while(i < 20):
        j = i*i
        if j < 4:
            i =  i+1
            continue
        print ('square:',j)
        i = i+1

func()