from __future__ import  print_function
#strip leading and trailing whitespace and substrins
s = "   ABCDEFGHIJKLMNOPQRSTUVWXYZ     "
print ("[", s, "]", sep=" ")
s = s.strip()
print ("[", s, "]",sep="")
#count occurrences of the substring "bcd"
print (s.count("BCD"))
