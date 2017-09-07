def linearSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found
bag = ['book','pencil','note book','sharpener','rubber']
item = input('what item do you want to check for in the bag?')
itemFound = linearSearch(item,bag)
if itemFound:
    print('yes, the item is in the bag')
else:
    print('Oops, your item seems not to be in the bag')