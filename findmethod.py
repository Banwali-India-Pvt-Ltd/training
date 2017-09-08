quote = 'Let it be, let it be, let it be'

result = quote.find('let it be')
print("substring 'let it':", result)

result = quote.find('small')
print("substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("contains substring 'be,'")
else:
    print("doesn't contain substring")