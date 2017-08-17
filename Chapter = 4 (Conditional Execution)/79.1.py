# Chapter -4 Conditional Exection
# 4.11.EXERCISES


i = input("Enter i?:- ")
j = input("Enter j?:- ")
k = input("Enter k?:- ")
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)
