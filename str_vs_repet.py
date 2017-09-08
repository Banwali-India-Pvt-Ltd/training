class A:
     def __init__(kuldeep):
       kuldeep.val = 10


     def __set__(kuldeep):
          return 'class A'


     def __repr__(kuldeep):
         return 'class A: kuldeep.val'
a = A()
print (a)
repr(a)
