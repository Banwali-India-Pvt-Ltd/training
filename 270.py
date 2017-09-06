from tester import Tester
#sort has a bug (it haa yet to be written!)
def sort(lst):
    pass#sort not yet implement)
def sum (lst):
    total = 0
    for i in range(1,len(lst)):
        total += lst[i]
    return total
def main():
    t = Tester()
    #make a test object
    #some test cases to test sort
    col = [4, 2, 3]
    sort(col);
    t. check_equals("Sort test#1",[2, 3, 4],col)
    col = [4, 2, 3]
    sort(col);
    t.check_equals("sort test #2",[2, 3, 4],col)
    #some test cases to test sum
    t.check_equals("sum test #1",sum([0, 3, 4]), 7)
    t.check_equals("sum test #2", sum ([-3, 0, 5]), 2)
