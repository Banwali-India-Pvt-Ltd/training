from   __future__ import  print_function
while True:
	print("Enter 'x' for exit.")
	n = input("Enter any number: ")
	if n == 'x':
		break
	else:
		val = int(n)
		nr = int(input("Upto how many rows: "))
		i = 0
		j = 0
		while i<nr:
			while j<i+1:
				print(val,end=" ")
				j = j + 1
			j = 0
			i = i + 1
			print()