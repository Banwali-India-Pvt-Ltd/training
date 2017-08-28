from time import  clock
print("enter your name: ", "")
start_time = clock()#I am confuse here , where from time will count as I've enter name sukhpal than print time 7.31 but when I've enter the name Rick then time get 7.24 , how it is counting .
name = input()
elapsed = clock() - start_time
print(name, "it took you", elapsed, "seconds to respond")