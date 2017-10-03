l = [1, 2, 3]
magic_number = 4
found = False

for n in l:
    if n == magic_number:
        found = True
        print("Magic number found")
        break

if not found:
    print("Magic number not found")