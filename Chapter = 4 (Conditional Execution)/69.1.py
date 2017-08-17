# Chapter -4 Conditional Execution
# 4.6 NESTED CONDITIONALS

value = eval(input("Please enter an integer value the range 0...10: "))
if value >= 0:
    if value <= 10:
        print(value, "is in range")
    else:
        print(value, "is too large")
else:
    print(value, "is to small")
print("Done")
