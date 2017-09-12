#introduction to operator overloading in ypthon
class vehicles:
    def __init__(self):
        self.number_of_vehicles = N
    def __add__(self, other):
        return self.number_of_vehicles + other.number_of_vehicles



v1 = vehicles(10)
v2 = vehicles(20)

print v1+v2