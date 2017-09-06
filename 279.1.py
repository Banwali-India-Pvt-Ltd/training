x = 0
while x < 100:
    try:
        x = int(input("please enter a small positive integer:"))
        print ("x =",x)
        if x < 5:
            a = None
            a[3] = 2
        elif x < 10:
            a = [0, 1]
            a[2] = 3
    except ValueError:
        print ("Input cannot be parsed as an integer")
    except TabError:
        print ("Trying to None as a valid object")
    except ImportError:
        print ("program continuse")
    print ("program finished")