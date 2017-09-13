# Arithmetic example

# The program doesn't gives a meaningful return
# It should calculate F to C but it returns only 0

degreesF = eval(raw_input('Enter the temperature in degrees F:'))

# perform the conversion

degreesC = 5/9*(degreesF - 32)

# Report the result

print(degreesF, "degrees F =", degreesC, 'degrees C')