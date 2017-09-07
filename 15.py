# About function

# Handle Keyword input separately
def sum (x,y):
    add = x+y         # Add to integer value
    sentence = 'The add of {} and {} is {}.'.format(x,y,add)
    print(sentence)

def main():
    sum(2,3)          # Call the sum function
    sum(4545, 5455)   # Call the sum function again
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sum(a,b)          # Call the sum function again

main()  # Call the main function