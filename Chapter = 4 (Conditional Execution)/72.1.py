# Chapter -4 Conditional Execution
# 4.7. MULTI-WAY DECISION STATEMENTS

value = eval(input("please enter an integer in the range 0...5: "))
if value < 0:
    print("Too small")
elif value == 0:
    print ("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print ("five")
else:
    print("Too large")
print("Done")