from  math import *
loop = True
while loop == True:
    adj = raw_input('adj(y): ')
    opp = raw_input('app(x): ')
    loop = False
    try:
        adj = float (adj)
    except:
        print 'Error: Could not convert adj to float, please enter a valid number. '
        loop = True
    try:
        opp = float (adj)
    except:
        print 'Error: Could not convert adj to float, please enter a valid number.'
        loop = True
    print '\n'
print '\n'
hyp = sqrt(adj **2+opp**2)



