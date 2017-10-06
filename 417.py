for x in (None,3,4.5,"foo",lambda : "moo",object,object()):
    print "{0}  ({1})".format(x,type(x))