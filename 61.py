x = 10
def f():
    def g():
        global x
        x = 1
    g ()
    print ('x', x)
f()