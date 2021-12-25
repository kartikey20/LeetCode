import statistics


def solve(matrix):
    xcoords = []
    ycoords = []
    m = len(matrix[0])
    n = len(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                xcoords.append(j)
                ycoords.append(i)
    x = statistics.median(xcoords)
    y = statistics.median(ycoords)
    return [int(x), int(y)]
