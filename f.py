print ("This program will take several numbers, then average them.")
count = int(input("How many numbers would you like to sum:  "))
current_count = 0

while current_count < count:
    print ("Number", current_count)
    number = float(input("Enter a number:  "))
    sum = sum + number
    current_count += 1

print("The average was:", sum / count)

# Prints the average value.

print ("Welcome to the average calculator program")
print ("NOTE- THIS PROGRAM ONLY CALCULATES AVERAGES FOR 3 NUMBERS")
x = int(input("Please enter the first number "))
y = int(input("Please enter the second number "))
z = int(input("Please enter the third number "))
str = x + y + z
print (float(str / 3.0))
# MADE BY SANJITH sanrubik@gmail.com