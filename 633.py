lst = [1,2,3,1,2,3,4,5,6,2,3,4]
str = "kuldeep"
from collections import Counter
print Counter(lst)
print Counter(str)


str = "who are you my this is may  how may this frand"
word = str.split()
print Counter(word)
c = Counter(word)
print c.most_common(4)




