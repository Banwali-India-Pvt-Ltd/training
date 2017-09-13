#python nested function
def f():
    x = 10
    def g():
        x = 15
        return x*x
    print ('x*x=', g())
f()