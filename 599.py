import time
t = time.localtime()
print time.asctime(t)



print time.ctime()


print time.gmtime()

print time.localtime()



t = (2016, 11,  16,  3,  38,  1,  48,  0)
secs = time.mktime(t)
print secs
print time.asctime(time.localtime(secs))
