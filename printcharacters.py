from __future__ import  print_function
s = "ABCDEFGHIJK"
print(s)
for i in range(len(s)):
    print("[", s,[i], "]", sep="", end="")
print()        # print newline

for ch in s:
    print("[", ch, ">", sep="", end="")
print()        # print newline
