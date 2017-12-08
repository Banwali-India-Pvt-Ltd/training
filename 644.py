class MyClass:
    "this is my secnd class"
    a = 10
    def func(self):
        print ('hello')
ob = MyClass()
print (MyClass.func)
print (ob.func)
ob.func()