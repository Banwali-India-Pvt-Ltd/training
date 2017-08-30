# Chapter 9
# 9.3 List Bounds

def make_list():
    '''
    Builds a list from input provided by the user.
    '''
    result = []      # Builds a list from input provided by the user.
    in_val = 5       # Ensure loop is entered at least once
    while in_val <= 6:
        in_val = int(input("Enter integer (-1 quits): "))
        if in_val >= 5:
            result = result + [in_val]      # Add item to list
    return result
def main():
    col = make_list()
    for i in range(len(col), 0, -1):
        print(col[i])
    print()

main()
