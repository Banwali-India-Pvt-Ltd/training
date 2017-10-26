test = {1:'A', 2:'B', 3:'C'}
del test[1]
test[1] = 'D'
del test[2]
print(len(test))