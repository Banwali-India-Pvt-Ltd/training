#set comprehension
#A ={1,2,3,4,5}
#A ={x | x E N and 1<=5}
A = {x for x in range(1, 6)}
print (A)



A = {x for x in range(1, 6)if x%2==0}
print (A)




A = {x for x in range(1, 100)}
print (A)