# The program returns the values without continue example
sum = 0
done = False;
while not done:
    val = eval(raw_input("Enter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
    else:
        if val != 999:
            print("Tallying", val)
            sum += val
        else:
            done = (val == 999);  # 999 entry exits loop
print("sum =", sum)