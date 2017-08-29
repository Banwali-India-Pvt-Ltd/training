def prompt():
    value = int(input("please enter an integer value: "))
    return value
print("This program adds together two integers.")
value1 = prompt()
value2 = prompt()
sum = value1 + value2
print(value1, "+", value2, "=", sum)