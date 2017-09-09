#Encapsulation: data hiding]
class speed:
    def __int__(self):
        self.__speed_ = 10
        self.__speed_limit = 20

    def get_speed(self):
        return self.speed

    def get_speed_limit(self):
        return self.__speed_limit

    def set_speed_limit(self,now_speed_limit):
        self.__speed_limit = new_speed_limit

s = speed()
s.speed = 100
s.__speed_limit = 50
s.set_speed_limit()
print (s.get_speed(),s.get_speed_limit())


