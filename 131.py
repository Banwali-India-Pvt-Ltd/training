from math import  sqrt, sin, cos, pi
p_x = 100
p_y = 0
radians = 10 * pi/180
cos10 = cos(radians)
sin10 = sin(radians)
x, y = eval(input("enter initial satellite coordinates (x, y):"))
d1 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y))
x_old = x;
x = x*cos10 - y*cos10
y = x_old*sin10 + y*cos10
d2 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - Y))
print("difference in distances: %.3f" % (d2 - d1))
