from __future__ import  print_function
def main():
    data = [10, 20, 30, 40, 50, 60]

    # Print the individual elements with negative indices
    print(data[-1])
    print(data[-2])
    print(data[-3])
    print(data[-4])
    print(data[-5])
    print(data[-6])

    print('------')

    # Print the list contents using negative indices
    for i in range(-1, -len(data) -1, -1):
        print(data[i], end=' ')
    print()

main()    # Execute main