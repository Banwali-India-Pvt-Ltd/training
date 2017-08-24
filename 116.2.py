in_value = 0
attempts = 0
while in_value < 1 or in_value > 10:
    in_value = int(input("please inter an integer in the range 0-10: " ))
    attempts += 1
tries = "try" if attempts == 1 else "tries"
print("it took you", attempts, tries, "to enter a valid number")

