counter = 0
while True:
  lineIn = input()
  if lineIn == 'END':
    break
  counter = counter+1
  print('line', counter, '=', lineIn)