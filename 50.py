#  File faultytempconv.py

#  Establish some variables
degreesf, degreesc = 0, 0
#  define the relationship between f and c
degreesc = 5/9*(degreesf - 32)
#  prompt user for degrees f
degreesf = eval(input('enter the temperature in degrees f: '))
#  report the result
print(degreesf, "degrees f =', degrees c")
