done = False
n, m = 0, 200
while not done and n != m:
    n = eval(input())
    if n < 0:
        done = True
        print('n =', n)
        