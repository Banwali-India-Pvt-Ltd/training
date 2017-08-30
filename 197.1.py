# Chapter 9

def main():
    data = [10, 20, 30, 40, 50, 60]
    # Print the individual elements with negative indices
    print(data[-1])     # Print 60
    print(data[-2])     # Print 50
    print(data[-3])     # Print 40
    print(data[-4])     # Print 30
    print(data[-5])     # Print 20
    print(data[-6])     # Print 10

    print('------')

    # Print the list contents in reverse using negative indices
    for i in range (-1, -len(data) -1, -1):
        print(data[i])
    print()           # Print newline

main()    # Execute main
