from __future__ import  print_function
# Strip leading and trailing whitespace and count substrings
s = ("      ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ      ")
print("[", s, "]", sep="")
s = s.strip()
print("[", s, "]", sep="")

# count occurrences of the substring "BCD"
print(s.count("BCD"))
