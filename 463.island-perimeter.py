#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
from copy import deepcopy
# @lc code=start


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        def valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == 1

        def bfs(start, visited):
            queue = [start]
            visited[start[0]][start[1]] = True
            perimeter = 0
            for elem in queue:
                row, col = elem
                for x, y in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                    if valid(x, y):
                        if not visited[x][y]:
                            visited[x][y] = True
                            queue.append([x, y])
                    else:
                        perimeter += 1
            return perimeter

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    return bfs([row, col], deepcopy(visited))

            # @lc code=end
