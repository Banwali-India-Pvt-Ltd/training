b=input("what number would you like to add ")
convert1= lambda b: str(int(b, 2))

a=input("what number would you like to add to it ")
convert= lambda a: str(int(a, 2))

c=(b+a)
print (c)
convert=lambda c: str(int(c, 2))
print ("Your binary numbers added together is" + convert(c))





num1 = input("what number would you like to add ")
a = int(num1, 2)

num2 = input("what number would you like to add to it ")
b = int(num2, 2)

ans = bin(a+b)
print("Your addition of numbers, in binary is " + ans)