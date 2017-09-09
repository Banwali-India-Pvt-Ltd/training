#python continue atatement
#continue is used inside a lope
I = [1, 2, 3, 4, 5, 10, 4, 5, 2, 1, 22]
def first_greater_or_equal_10(lst):
    for i in lst:
        if i < 10:
           continue
        return i
print (first_greater_or_equal_10(1))