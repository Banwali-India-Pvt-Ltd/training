for first in 'ABC':
    for second in 'ABC':
        if second != first:
            for third in 'ABC':
                if third != first and third != second:
                    print(first + second + third)