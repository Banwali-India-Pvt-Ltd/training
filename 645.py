class car(object):
    wheels = 4
    def __init__(self,make,model):
        self.make = make
        self.modulel = model
mustang = car('ford','mustang')
print mustang.wheels
print car.wheels
