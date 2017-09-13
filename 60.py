#python nonlocal keword
def f():
    x = 10
    def g():
        x = 1
    g()
    print ('x=',x)
f ()