def numberofDistinctIslands(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    count = 0
    path_set = set()

    def valid(row, col):
        return 0 <= row < row_len and 0 <= col < col_len and not visited[row][col]

    def bfs(start):
        queue = [[start, []]]
        visited[start[0]][start[1]] = True
        for elem in queue:
            row, col = elem[0]
            path = elem[1]
            for y, x in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r, c = row+y, col+x
                if valid(r, c) and not grid[r][c] == 0:
                    visited[r][c] = True
                    queue.append([[r, c], path + [(y, x)]])
            print(path)
        return path

    for row in range(row_len):
        for col in range(col_len):
            if valid(row, col) and grid[row][col] == 1:
                path = tuple(bfs([row, col]))
                print(path)
                if path not in path_set:
                    path_set.add(path)
                    count += 1
    return count


print(numberofDistinctIslands([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]))
