def eg1_for(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat

def eg1_lc(matrix):
    return [x for row in matrix for x in row ]
matrix = [ range(0,5), range(5,10), range(10,15) ]
print "Original Matrix: " + str(matrix)
print "FOR-loop result: " + str(eg1_for(matrix))
print "LC result      : " + str(eg1_lc(matrix))