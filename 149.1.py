num1 = int(input('please enter an enteger: '))
num2 = int(input('please enter another integer: '))
min = num1 if num1 < num2 else num2
largest_factor = 1
for i in range(1, min + 1):
    if num1 % i == 0 and num2 % i == 0:
        largest_factor = i
print(largest_factor)
