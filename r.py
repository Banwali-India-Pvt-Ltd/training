# so lets start by creating a list and fill it with all the numbers we need
numbers = list()
for i in range(0, 10):
    inputNr = int(input("Enter a number: "))
    if(inputNr == -99):
        break;

    numbers.append(inputNr)

#Then we take all of the numbers and calculate the sum and avg on them
sum = 0
for j, val in enumerate(numbers):
    sum += val

print("The total sum is: " + str(sum))
print("The avg is: " + str(sum / len(numbers)))