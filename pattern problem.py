print ("my question no.1")
def main():
	size = 5
	for i in range(6):
		print ('* ' * size)
main()
print ("my question no.2")
def pattern(n):
	for x in range(n, 0, -1):
		print ("*" * x)
pattern(7)

print ("my question no.3")
def pattern1(n):
    print "\n".join("*" * x for x in range(n, 0, -1))
pattern1(10)

print ("my question no.4")
def main():
    for i in range(1,6):
        b = str(i)
        a = (b * 5)
        print (" ".join(a))
main()

print ("my question no.5")
def main():
    for i in range(6):
        print (str(i) + " ")*i
main()

print ("my question no.6")
def main():
    col = "12345"
    for i in range(5):
        y = col * 1
        print " ".join(y)
main()

print ("my question no.7")
def main():
    col = "ABCDE"
    place = 0
    for i in range(5):
        x = col[place]
        y = x * 5
        place += 1
        print " ".join(y)

main()

print ("my question no.8")
def main():
    col = "ABCDE"
    for i in range(4):
        y = col * 1
        print " ".join(y)
main()

print ("my question no.9")
def main():
    x = "12345"
    y = 4
    for i in range(5):
        z = x[y]
        a = z * 5
        print (" ".join(a))
main()

print ("my question no.10")
def main():
    col = "54321"
    for i in range(5):
        y = col * 1
        print " ".join(y)
main()

print ("my question no.11")
def main():
    col = "EDCBA"
    for i in range(5):
        y = col * 1
        print " ".join(y)
main()

print ("my question no.12")
def main():
    for i in range(0, 5):
        for j in range(0, i+1):
            print ("*"),
        print ("\r")
main()

print ("my question no.13")
def main():
    for i in range(0, 6):
        for j in range(1, i+1):
            print (i),
        print ("\r")
main()

print ("my question no.14")
def main():
    for i in range(1, 6):
        x = str(i)
        y = x * i
        print(" ".join(y))
main()

print ("my question no.15")
def main():
    col = "12345"
    place = 0
    lastP = 1
    for i in range(1,6):
        b = col[place:lastP]
        c = b * 1
        lastP += 1
        print " ".join(c)
main()

print ("my question no.16")
def main():
    pat = "ABCDE"
    col = 1
    for i in range(5):
        x = pat[i]
        y = x * col
        col += 1
        print " ".join(y)
main()