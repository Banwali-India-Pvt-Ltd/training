# The program section of code assigns the indicated values to a bool

x = 10
y = 20

b = (x == 10)  # assign true to b
b = (x != 10)    # assigns false to b
b = (x == 10 and y == 20)  # assigns true to b
b = (x != 10 and y == 20)  # assigns false to b
b = (x == 10 and y != 20)  # assign false to b
b = (x != 10 and y != 20)  # assign false to b
b = (x == 10 or y == 20)  # assign true to b
b = (x != 10 or y == 20)  # assign true to b
b = (x == 10 or y != 20)  # assign true to b
b = (x != 10 or y != 20)  # assign false to b
