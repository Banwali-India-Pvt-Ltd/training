x = 0
while x < 100:
    try:
        # I hope the user enters a valid python integer!
        x = int(input("please enter a small positive integer: "))
        print("x =", x)
        if x < 5:
            a = None
            a[3] = 2   # Using None as a populated list!
        elif x < 10:
            a = [0, 1]
            a[2] = 3   # Exceeding the list's bounds
    except ValueError:
        print("Input cannot be parsed as an integer")
    except TypeError:
        print("Trying to use a None as a valid object")
    except IndexError:
        print("Straying from the bounds of the list")
    print("Program continues")
print("Program finished")