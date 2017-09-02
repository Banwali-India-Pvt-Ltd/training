# Chapter 11 ( Objects )
# String objects

# This code run time show Returns a string right justified within a field padded with a specified character which defaults to a space
word = "ABCD"
print(word.rjust(10, "*"))
print(word.rjust(3, "*"))
print(word.rjust(15, ">"))
print(word.rjust(10))