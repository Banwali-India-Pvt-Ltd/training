# Chapter 12 (Custom Types)
# 12.3.1 Stopwatch

def binary_search(lst, seek):
    # Returns the index of element seek in list lst,
    # if seek is present in lst.
    # lst must be in sorted order.
    # Returns None if seek is not an element of lst.
    # lst is the lst in which to search.
    # seek is the element to find.
    first = 0                    # Initially the first element in list
    last = len(lst) - 1          # Initially the last element in list
    while first <= last:
        # mid is middle of the list
        mid = first + (last - first +1)//2      # Note: Integer division
        if lst[mid] == seek:
            return mid           # Found it
        elif lst[mid] > seek:
            last = mid - 1       # continue with 1st half
        else: # v[mid] < seek
            first = mid + 1      # continue with 2nd half
    return None         # Not there

def ordered_linear_search(lst, seek):
    # Returns the index of element seek in list lst,
    # if seek is present in lst.
    # lst must be in sorted order.
    # Returns None if seek is not an element of lst.
    # lst is the lst in which to search.
    # seek is the element to find.

    i = 0
    n = len(lst)
    while i < n and lst[i] <= seek:
        if lst[i] == seek:
            return i          # Return position immediately
        i += 1
    return None               # Element not found

def test_searches(lst):
    from stopwatch import Stopwatch

    timer = Stopwatch
    # Find each element using ordered linear search
    timer.start()       # Start the clock
    n = len(lst)
    for i in range(n):
        if ordered_linear_search(lst, i) != i:
            print("error")
    timer.stop()          # Stop the clock
    print("Linear elapsed time", timer.elapsed())

    # Find each element using binary search
    timer.reset()           # Reset the clock
    timer.start()           # Start the clock
    n = len(lst)
    for i in range(n):
        if binary_search(lst, i)!= i:
            print("error")
    timer.stop()
    print("Binary elapsed time", timer.elapsed())
def main():
    SIZE = 20000
    test_list = list(range(SIZE))
    test_searches(test_list)

main()