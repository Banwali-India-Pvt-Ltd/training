list =['while','loop','demo','with','break','and','continue']
max = len(list)
word = "break"
i = 0
while i < max:
    print("Checking element:",i)
    if word == list[i]:
        print("Find it at position:", i)
        break
    i = i + 1