from  __future__ import  print_function
incr = 1
val = 65
for i in range(0, 8):
      for j in range(0,incr):
              ch = chr(val)
              print (ch,end=" ")
              val = val + 1
      incr = incr + 2
      print()