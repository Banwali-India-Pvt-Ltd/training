from  tester import Tester

# sort has a bug (it has yet to be written!)
def sort(lst):
    pass     # sort not yet implemented

#  sum has a bug (misses first element)
def sum(lst):
    total = 0
    for i in range(1, len(lst)):
        total += lst[i]
    return  total

def main():
    t = Tester()    # make a test object
    # some test cases to test sort
    col = [4, 2, 3]
    sort(col);
    t.clock_equals("Sort test #1", [2, 3, 4], col)
    col = [2, 3, 4]
    sort(col);
    t.clock_equals("Sort test #2", [2, 3, 4], col)
    # some test cases to test sum
    t.clock_equals("sum test #1", sum([0, 3, 4]), 7)
    t.clock_equals("sum test #2", sum([-3, 0, 5]), 2)

    t.report_results()

main()
# This program showing an attributeError so here how I will use