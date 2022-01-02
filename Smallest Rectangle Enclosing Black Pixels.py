from copy import deepcopy


def minArea(image, x, y):
    row_len = len(image)
    col_len = len(image[0])
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    max_x = [0]
    max_y = [0]

    def valid(row, col, visited):
        return 0 <= row < row_len and 0 <= col < col_len and \
            not visited[row][col] and image[row][col] == "1"

    def bfs(start, visited):
        visited[start[0]][start[1]] = True
        y_dir = 1  # row
        x_dir = 1  # col
        queue = [[start, y_dir, x_dir]]
        for node in queue:
            row, col = node[0]
            _y = node[1]  # row
            _x = node[2]  # col

            if valid(row-1, col, visited):
                visited[row-1][col] = True
                queue.append([[row-1, col], _y-1, _x])

            if valid(row+1, col, visited):
                visited[row+1][col] = True
                queue.append([[row+1, col], _y+1, _x])

            if valid(row, col+1, visited):
                visited[row][col+1] = True
                queue.append([[row, col+1], _y, _x+1])

            if valid(row, col-1, visited):
                visited[row][col-1] = True
                queue.append([[row, col-1], _y, _x-1])

            x_dir = max(x_dir, _x)
            y_dir = max(y_dir, _y)

        max_x[0] = max(max_x[0], x_dir)
        max_y[0] = max(max_y[0], y_dir)

    for row in range(row_len):
        for col in range(col_len):
            if image[row][col] == '1':
                bfs([row, col], deepcopy(visited))

    return max_y[0] * max_x[0]
