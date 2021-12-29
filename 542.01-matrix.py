#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])

        def valid(row, col):
            if 0 <= row < row_len and 0 <= col < col_len:
                return True
            return False

        def bfs(start):
            queue = [start]
            for node in queue:
                row, col, dist = node

                if mat[row][col] == 0:
                    return dist

                if valid(row+1, col):
                    queue.append([row+1, col, dist+1])

                if valid(row-1, col):
                    queue.append([row-1, col, dist+1])

                if valid(row, col+1):
                    queue.append([row, col + 1, dist+1])

                if valid(row, col-1):
                    queue.append([row, col-1, dist+1])

        res = [[0 for _ in range(col_len)] for _ in range(row_len)]
        for row in range(row_len):
            for col in range(col_len):
                if mat[row][col] == 1:
                    res[row][col] = bfs([row, col, 0])
        return res

# @lc code=end
