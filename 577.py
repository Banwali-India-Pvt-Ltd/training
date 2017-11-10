from  __future__  import  print_function
n = int(input("please enter the number,=>"))
decr = 8
count = 64
val = 65
for i in range(0, 5):
	for k in range(0, decr):
		print(end=" ")
	for j in range(0, i+1):
		count = count + 1
	val = count
	temp = val
	for j in range(0, i+1):
		ch = chr(val)
		print(ch, end=" ")
		val = val - 1
	val = temp
	decr = decr - 2
	print()
