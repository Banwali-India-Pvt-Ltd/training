number = int(input("Enter an integer: "))
if number < 100:
    print("Your number is smaller than 100")
else:
    print("Your number is greater than 100")



amount = float(input("Enter amount: "))
inrate = float(input("Enter Interest rate: "))
period = int(input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year %d Rs. %.2f" % (year, value))
    amount = value
    year = year + 1



