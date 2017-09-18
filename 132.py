N = 10
sum = 0
count = 0
while count < N:
    number = float(input(""))
    sum = sum + number
    count = count + 1
average = float(sum)/N
print("N = %d , Sum = %f" % (N, sum))
print("Average = %f" % average)






fahrenheit = 0.0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = ( fahrenheit - 32.0 ) / 1.8 # Here we calculate the Celsius value
    print("%5.1f %7.2f" % (fahrenheit , celsius))
    fahrenheit = fahrenheit + 25