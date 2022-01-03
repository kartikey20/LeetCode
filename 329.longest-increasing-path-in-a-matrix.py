#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
from copy import deepcopy


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])
        seen = [[False for _ in range(col_len)] for _ in range(row_len)]
        max_path = 0

        def valid(row, col, visited):
            return 0 <= row < row_len and 0 <= col < col_len and not visited[row][col]

        def bfs(start, visited):
            visited[start[0]][start[1]] = True
            queue = [[start, 1]]
            max_path_count = 0
            for node in queue:
                row, col = node[0]
                path = node[1]

                if valid(row+1, col, visited) and matrix[row+1][col] > matrix[row][col]:
                    visited[row+1][col] = True
                    queue.append([[row+1, col], path+1])

                if valid(row-1, col, visited) and matrix[row-1][col] > matrix[row][col]:
                    visited[row-1][col] = True
                    queue.append([[row-1, col], path+1])

                if valid(row, col-1, visited) and matrix[row][col-1] > matrix[row][col]:
                    visited[row-1][col] = True
                    queue.append([[row, col-1], path + 1])

                if valid(row, col+1, visited) and matrix[row][col+1] > matrix[row][col]:
                    visited[row][col+1] = True
                    queue.append([[row, col+1], path+1])

                max_path_count = max(max_path_count, path)
                print(queue)
            return max_path_count
        # print(bfs([2, 1], visited))
        print(bfs([2, 1], seen))
        # for row in range(row_len):
        #     for col in range(col_len):
        #         max_path = max(max_path, bfs([row, col], deepcopy(visited)))
        # return max_path
# [  [7,8,9],
#    [9,7,6],
#    [7,2,3]]

# @lc code=end
