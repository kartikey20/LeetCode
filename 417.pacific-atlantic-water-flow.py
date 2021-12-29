#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len = len(heights)
        col_len = len(heights[0])
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]
        res = []

        def bfs(start, visited):
            pacific = False
            atlantic = False
            visited[start[0]][start[1]] = True
            queue = [start]
            for node in queue:
                row, col = node
                if not visited[row+1][col] and heights[row+1][col] <= heights[row][col]:
                    visited[row+1][col] = True
                    queue.append([row+1, col])

                if not visited[row-1][col] and heights[row-1][col] <= heights[row][col]:
                    visited[row-1][col] = True
                    queue.append([row-1, col])

                if not visited[row][col+1] and heights[row][col+1] <= heights[row][col]:
                    visited[row][col+1] = True
                    queue.append([row, col+1])

                if not visited[row][col-1] and heights[row][col-1] <= heights[row][col]:
                    visited[row][col-1] = True
                    queue.append([row, col-1])

                if col == 0 or row == 0:
                    if not pacific:
                        pacific = True
                if col == col_len-1 or row == row_len-1:
                    if not atlantic:
                        atlantic = True

                if pacific and atlantic:
                    res.append([row, col])
                    break

        bfs([0, 0], visited)

# @lc code=end
