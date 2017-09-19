

#Asks for a number.
#Prints if it is even or odd

print ("Input [x] for exit.")

while True:
	inp = input("Tell me a number: ")
	if inp == 'x':
		break
	# catch any resulting ValueError during the conversion to float
	try:
		number = float(inp)
	except ValueError:
		print('I said: Tell me a NUMBER!')
	else:
		test = number % 2
		if test == 0:
			print (int(number),"is even.")
		elif test == 1:
			print (int(number),"is odd.")
		else:
			print (number,"is very strange.")

