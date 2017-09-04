def main():
    sun = 0.0
    NUMBERS_OF_INTEGERS = 5
    print("please enter", NUMBERS_OF_INTEGERS, " numbers: ")
    for i in range(0, NUMBERS_OF_INTEGERS):
        num = eval(input("enter number " + str(i) + ": "))
        sum += num;
    print("Average:", sum/NUMBERS_OF_INTEGERS)
main() # There is an error showing in line number 7 .why?