class Rational:
    def __init__(self,num,den):
        self. _numerator = num
        if den !=0:
            self._denominator = den
        else:
            print ("Attempt to make an illegal rational number")
            from sys import exit
            exet(1)
    def get_numerator (self):
        return self.__numerator
    def get_denominator(self):
        return self.__denominator
    def set_numeratoe(self,n):
        self.__numerator = n
    def set_denominator (self,d):
        if d !=0:
            self.__denominator = d
        else:
            print ("Error: zero denominator!")
            from sys import exit
            exit(1)
    def __str__(self):
        return str (self. get_numerator()) + "/" + str (self.get_denominator())
def main():
     fract1 = Rational(1, 2)
     fract2 = Rational(2, 3)
     print ("fract1 =", fract1)
     print ("fract2 =", fract2)
     fract1.set_numeratoe(3)
     fract1.set_denominator(4)
     fract2.set_numeratoe(1)
     fract2.set_denominator(10)
     print ("fract1 =", fract1)
     print ("fract2 =", fract2)
main()










