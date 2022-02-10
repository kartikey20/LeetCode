#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
import queue


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row_len = len(heights)
        col_len = len(heights[0])
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        def valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and not visited[row][col]

        def bfs(start):
            visited[start] = True
            queue = [start]
            for node in queue:
                row, col = node
                for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if valid(row+r, col+c) and :
                        # @lc code=end
