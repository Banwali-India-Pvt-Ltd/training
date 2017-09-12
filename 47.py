#global keyword
#global variabale means a variaable defined outside any scope any of class
#or a functiuon
i = 10
def p():
    print (i)


def incr():
    global i
    i = 11
    print (i)

p()
incr()
p()


