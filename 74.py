basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(input("Enter the number of inputs sold: "))
price = float(input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print("Bonus = %6.2f" % bonus)
print("Commision = %6.2f" % commision)
print("Gross salary = %6.2f") % (basic_salary + bonus + commision)







number = int(input("Enter a number: "))
if number < 100:
   print("The number is less than 100")
else:
    print("The number is greater than 100")