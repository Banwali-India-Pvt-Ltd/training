#!/usr/bin/env python
from math import *

user_func = raw_input("type a function: y = ")

for x in range(1,10):
	print "x = ", x , ", y = ", eval(user_func)



from math import *

hidden_value = "this is secret"

def dangerous_function(filename):
	print open(filename).read()

user_func = raw_input("type a function: y = ")

for x in range(1,10):
	print "x = ", x , ", y = ", eval(user_func)