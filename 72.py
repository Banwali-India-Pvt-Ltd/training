value = eval(input("please enter an integer in the range 0...5: "))
if value < 0:
    print("too small")
elif value == 0:
    print("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print("five")
else:
    print("too large")
print("done")