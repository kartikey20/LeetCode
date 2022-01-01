from copy import deepcopy


def wallsAndGates(rooms):
    # write your code here
    row_len = len(rooms)
    col_len = len(rooms[0])

    inf = 2**31 - 1

    def bfs(start, seen):

        def valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and \
                not seen[row][col] and not rooms[row][col] == -1

        seen[start[0]][start[1]] = True
        dist = 0
        queue = [[start, dist]]
        for node in queue:
            row, col = node[0]
            dist = node[1]

            if valid(row+1, col):
                seen[row+1][col] = True
                queue.append([[row+1, col], dist+1])

            if valid(row-1, col):
                seen[row-1][col] = True
                queue.append([[row-1, col], dist+1])

            if valid(row, col+1):
                seen[row][col+1] = True
                queue.append([[row, col+1], dist+1])

            if valid(row, col-1):
                seen[row][col-1] = True
                queue.append([[row, col-1], dist+1])

            if rooms[row][col] == 0:
                return dist

    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    for row in range(row_len):
        for col in range(col_len):
            if rooms[row][col] == inf:
                val = bfs([row, col], deepcopy(visited))
                rooms[row][col] = val if val else inf
    return rooms
