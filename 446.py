points = [[10,10]], [20,20],[30,30],[40,40]
middle = points[1:-1]
middle[0][0] = 'whoops'
middle[1][0] = 'aliasing'
print middle
print points