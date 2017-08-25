x = 100
while x > 0:
    y = eval(input())
    if y == 25:
        x += 1
        continue
        x = eval(input()) # if here we will use break than cannot print only y == value as here 25 .
        print('x =', x)
