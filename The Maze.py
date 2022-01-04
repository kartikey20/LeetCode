
from copy import deepcopy


def hasPath(maze, start, destination):
    row_len = len(maze)
    col_len = len(maze[0])
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]

    def valid(row, col):
        return 0 <= row < row_len and 0 <= col < col_len and not maze[row][col] == 1

    def not_valid(row, col):
        return row < 0 or row >= row_len or col < 0 or col >= col_len

    def bfs(start, dx, dy, visited):
        queue = [[start, dx, dy, 0]]
        visited[start[0]][start[1]] = True
        for x in queue:
            row, col = x[0]
            x_dir = x[1]
            y_dir = x[2]
            steps = x[3]
            # print(row+y_dir, col+x_dir)
            if [row, col] == destination:
                return steps
            elif not_valid(row+y_dir, col+x_dir) or maze[row+y_dir][col+x_dir] == 1:
                for r, c in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    if valid(row + r, col + c) and not visited[row + r][col + c]:
                        visited[row+r][col + c] = True
                        queue.append([[row+r, col+c], c, r, steps+1])
            else:
                visited[row+y_dir][col+x_dir] = True
                queue.append([[row+y_dir, col+x_dir], x_dir, y_dir, steps+1])
        return float('inf')

    start_row, start_col = start
    min_steps = float('inf')
    for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if valid(start_row+y, start_col+x):
            min_steps = min(min_steps, bfs([start_row+y, start_col+x], x, y, deepcopy(visited)))
    return min_steps + 1


print(hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [0, 0]))
