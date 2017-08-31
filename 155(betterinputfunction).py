def get_int_in_range(first, last):
    if first > last:
        first, last = last, first
    in_value = int(input("please enter values in the range " + str(first) + "..." + str(last) + ": "))
    while in_value < first or in_value > last:
        print(in_value, "is not in range", first, "...", last)
        in_value = int(input("please try again: "))
def main():
    print(get_int_in_range(10, 20))
    print(get_int_in_range(20, 10))#why no showing this parameter when I run this program
    print(get_int_in_range(5, 5))
    print(get_int_in_range(-100, 100))
main()