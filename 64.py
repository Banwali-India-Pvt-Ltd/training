#parameter passing in python
#passing parameter by name
def record(name, id_no):
    print name, id_no
record(name='foo', id_no= 10)



def record(name, id_no):
    print name, id_no
record( id_no= 10, name= 'foo')