no_of_rows = int(input())
grid = []
for _ in range(no_of_rows):
    grid.append(list(map(int, input().split())))


def solve(matrix):
    col_len = len(matrix[0])
    row_len = len(matrix)
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]

    def valid(row, col):
        return 0 <= row < row_len and 0 <= col < col_len

    paths = []

    def dfs(row, col, diff, path, visited):
        visited[row][col] = True
        path.append(matrix[row][col])
        if valid(row+1, col) and not visited[row+1][col] and abs(matrix[row][col] - matrix[row+1][col]) == diff:
            dfs(row+1, col, diff, path[:], visited[:])
        if valid(row-1, col) and not visited[row-1][col] and abs(matrix[row][col] - matrix[row-1][col]) == diff:
            dfs(row-1, col, diff, path[:], visited[:])
        if valid(row, col+1) and not visited[row][col+1] and abs(matrix[row][col] - matrix[row][col+1]) == diff:
            dfs(row, col+1, diff, path[:], visited[:])
        if valid(row, col-1) and not visited[row][col-1] and abs(matrix[row][col] - matrix[row][col-1]) == diff:
            dfs(row, col-1, diff, path[:], visited[:])
        if row == row_len-1 and col == col_len-1:
            paths.append([path, diff])

    dfs(0, 0, abs(matrix[1][0] - matrix[0][0]), [], visited[:])
    dfs(0, 0, abs(matrix[0][1] - matrix[0][0]), [], visited[:])
    return paths


print(solve(grid))
