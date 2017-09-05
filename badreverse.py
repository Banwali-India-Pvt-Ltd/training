from __future__ import  print_function
def make_list():
    '''
    Builds a list from input provided by the user.
    '''
    result = []     # List to return is initially empty
    in_val = 0      # Ensure loop is entered at least once
    while in_val >= 0:
        in_val = int(input("enter enteger (-1 quits): "))
        if in_val >= 0:
            result = result + [in_val]     # Add item to list
    return result

def main():
    col = make_list()
    # Print the list in the reverse
    for i in range(len(col), 0, -1):
        print(col[i], end=" ")
    print()

main()