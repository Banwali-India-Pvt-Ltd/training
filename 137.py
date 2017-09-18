def adder(*args):
	print adder,
	if type(args[0]) == type(0):
		sum = 0
	else:
		sum = args[0][:0]
	for arg in args:
		sum = sum + arg
	return sum

print adder(1,2,3,4,5,6,7,8,9)
print adder('spam','egg','toast')
print adder([1,2],[3,4])



def print_func( par ):
   print "Hello : ", par
   return