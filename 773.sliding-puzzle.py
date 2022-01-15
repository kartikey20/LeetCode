#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
from typing import List
# @lc code=start

from copy import deepcopy


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [[1, 2, 3], [4, 5, 0]]
        visited = set()
        row_len = len(board)
        col_len = len(board[0])

        def valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and (row, col) not in visited

        def bfs(start):
            queue = [[start, 0, board]]
            visited.add(start)
            for elem in queue:
                row, col = elem[0]
                count = elem[1]
                matrix = elem[2]
                print(matrix)
                if matrix == target:
                    return count

                for r, c in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    if valid(row+r, col+c):
                        visited.add((row+r, col+c))
                        matrix_copy = deepcopy(matrix)
                        matrix_copy[row][col], matrix_copy[row+r][col+c] = matrix_copy[row+r][col+c], matrix_copy[row][col]
                        queue.append([(row+r, col+c), count + 1, matrix_copy])
            return -1

        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == 0:
                    return bfs((row, col))


A = Solution()
print(A.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
# @lc code=end
