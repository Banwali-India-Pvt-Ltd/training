def fahrenheit(t):
    return ((float(9)/5) * t + 32)
def calsius(t):
    return ((float(9)/5) * (t-32))
temp = [0,22.5,40,100]
f_temp = map(fahrenheit,temp)
r_temp = map(calsius,temp)
print f_temp
print r_temp
