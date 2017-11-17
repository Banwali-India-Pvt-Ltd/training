import time
print time.ctime()
time.sleep(5)
print time.ctime()




t = (2017, 11, 16, 6, 30, 2, 48, 0)
t = time.mktime(t)
print time.strftime(time.gmtime(t))