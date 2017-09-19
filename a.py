# Perimeter of Square
def calculatePerimeter(l):
  return 4*l

# Area of Square
def calculateArea(l):
  return l*1

property = input("Type a function: ")

for l in range(1, 5):
    if (property == 'calculatePerimeter(l)'):
        print("If length is ", l , ", Perimeter = ", eval(property))
    elif (property == 'calculateArea(l)'):
	print("If length is ", l , ", Area = ", eval(property))
    else:
      print('Wrong Function')
      break