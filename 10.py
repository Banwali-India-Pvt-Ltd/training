#bubble sort
l = [8,2,4,1]
i = 0
print 'len(l)', len(l)
print 'before:', l
while i < len(l):
    j = 0
    while j < i:
        if l[i] < l[j]:
            #swap operation
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            j = j + 1
        i = i + 1


