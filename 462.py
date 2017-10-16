def sumProblem(x,y):
    sum = x + y
    sentence = 'the sum of {} and {}.'.format(x, y,sum)
    print (sentence)
def main():
    sumProblem(2,3)
    sumProblem(123456789012345,5346789344)
    a = int(input("Enter an integer:"))
    b = int(input("Enter another integer: "))
    sumProblem()
main()