class MyClass:
    classVar = 1
    def __init__(self, inVar):
        self.inVar = inVar
obj1 = MyClass("Ramesh")
obj2 = MyClass("Rahul")

print("Before Changing :")
print(obj1.classVar, obj1.inVar)

MyClass.classVar = 2
obj1.inVar = "Rakesh"
print("After Changing :")
print(obj1.classVar, obj1.inVar)