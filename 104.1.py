sum = 0
done = False;
while not done:
    val = eval(input("enter positive integer (999 quits):"))
    if val < 0 :
        print("negative value", val, "ignored")
        continue;
        if val != 999:
            print("tallying", val)
            sum += val
        else:
            done = (val == 999);
            print("sum =", sum)
