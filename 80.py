s = input("Enter a line: ")
print("The number of words in the line are %d" % (len(s.split(" "))))





#definig a function
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Enter a string: ")
    if palindrome(s):
        print("Yay a palindrome")
else:
     print("Oh no, not a palindrome")