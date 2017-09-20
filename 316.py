import dis

def comparison_1(a, b):
    if a == 5 and b == 5:
        pass

def comparison_2(a, b):
    if a == b and b == 5:
        pass

def comparison_3(a, b):
    if a == b == 5:
        pass

print("*** First comparison ***")
dis.dis(comparison_1)

print("\n*** Second comparison ***")
dis.dis(comparison_2)

print("\n*** Third comparison ***")
dis.dis(comparison_3)