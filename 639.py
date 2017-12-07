import time
print time.altzone

t = time.localtime()
print time.asctime(t)


print time.ctime()

print time.gmtime()

print time.localtime()

t = (2017,2,17,17,3,38,1,48,0)
secs = time.mktime(t)
print time.asctime(time.localtime(secs))


print time.ctime()


print time.ctime()
time.sleep(1)
print time


t = time.ctime()
print t