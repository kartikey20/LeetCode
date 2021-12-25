no_of_rows = int(input())
grid = []
for _ in range(no_of_rows):
    grid.append(list(map(int, input().split())))


def solve(matrix, no_of_rows):
    col_len = len(matrix[0])
    visited = [[False for _ in range(col_len)] for _ in range(no_of_rows)]
