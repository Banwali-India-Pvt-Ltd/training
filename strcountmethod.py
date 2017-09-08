# define string
string = " python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)

# define string
string = "python is awesome, isn't it?"
substring = "i"

# count after first 'i' the last 'i'
count = string.count(substring, 8, 25)

# print count
print("The count is:", count)