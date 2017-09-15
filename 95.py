# The program is based on continue statement which skip numbers
# when user enter any positive number besides 999
# then it takes values independtly
# when user enter any negative number then
# the compiler ignores that number & be continue
sum = 0
done = False;
while not done:
    val = eval(raw_input("Enter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
        continue;   # Skip rest of body for this iteration
    if val != 999:
        print("Tallying", val)
        sum +=  val
    else:
        done = (val == 999);  # 999 exits loop
print("sum =", sum)