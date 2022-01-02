from copy import deepcopy


def shortestDistance(grid):
    row_len = len(grid)
    minimum = float('inf')
    max_len = 0
    col_len = len(grid[0])
    seen = [[False for _ in range(col_len)] for _ in range(row_len)]

    def valid(row, col, visited):
        return 0 <= row < row_len and 0 <= col < col_len and \
            not visited[row][col] and not grid[row][col] == 2

    def bfs(start, visited):
        dist = 0
        cost = []
        queue = [[start, dist]]
        visited[start[0]][start[1]] = True

        for node in queue:
            row, col = node[0]
            dist = node[1]
            if valid(row+1, col, visited):
                if not visited[row+1][col]:
                    visited[row+1][col] = True
                    if grid[row+1][col] == 1:
                        cost.append(dist+1)
                    else:
                        queue.append([[row+1, col], dist+1])

            if valid(row-1, col, visited):
                if not visited[row-1][col]:
                    visited[row-1][col] = True
                    if grid[row-1][col] == 1:
                        cost.append(dist+1)
                    else:
                        queue.append([[row-1, col], dist+1])

            if valid(row, col+1, visited):
                if not visited[row][col+1]:
                    visited[row][col+1] = True
                    if grid[row][col+1] == 1:
                        cost.append(dist+1)
                    else:
                        queue.append([[row, col+1], dist+1])

            if valid(row, col-1, visited):
                if not visited[row][col-1]:
                    visited[row][col-1] = True
                    if grid[row][col-1] == 1:
                        cost.append(dist+1)
                    else:
                        queue.append([[row, col-1], dist+1])
        return cost

    all_dist = []
    for row in range(row_len):
        for col in range(col_len):
            if grid[row][col] == 0:
                val = bfs([row, col], deepcopy(seen))
                all_dist.append(val)

    max_len_arr = max(all_dist, key=len)
    max_len = len(max_len_arr)
    for x in all_dist:
        if len(x) == max_len:
            minimum = min(minimum, sum(x))
    return minimum


print(
    shortestDistance(
        [[1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 1, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 1],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]))

# print(sum([1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 9]))
