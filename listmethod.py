list = ['Amar', 'Ramesh', 'Samandar']
list.append('name')     # append elem at end
list.insert(0, 'xxx')    # insert elem at index 0
list.extend(['yyy', 'zzz'])   # add list of elems at end
print list
print list.index('Amar')



list.remove('Amar')    # search and remove that element
list.pop(1)             # removes and returns 'Samandar'
print list