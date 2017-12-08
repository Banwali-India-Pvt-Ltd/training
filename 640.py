class MyClass:
    classVar = 1
    def __init__(self,inVar):
        self.inVar = inVar
obj1 = MyClass("Ramesh")
obj2 = MyClass("Rahul")
print ("access class variable using class name:")
print ("access class variable using class object:")
print (obj1.classVar,obj1.inVar)
print (obj2.classVar,obj2.inVar)