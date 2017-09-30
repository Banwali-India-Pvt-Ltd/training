# if-else statement
a = 150
b = 50
c = 100
# symbolic execution
if a > b:  # line 6-9 is in the scope of line 5 (if a>b)
    if a > c:
        print 'a is greatest'
    else:
        print 'c is greatest from line9'
elif b > c: # line 11 is in the scope of line 10
    print 'b is greatest'
else: # line 13 is in the scope of line 12
    print 'c is greatest form line13'