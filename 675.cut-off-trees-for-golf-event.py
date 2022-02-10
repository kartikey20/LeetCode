# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start

from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row_len = len(forest)
        col_len = len(forest[0])
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        def valid(row, col):
            if 0 <= row < row_len and 0 <= col < col_len and not visited[row][col] and not forest[row][col] == 0:
                return True
            return False

        def bfs(start):
            visited[start[0]][start[1]] = True
            queue = [start]
            dist = start[2]

            for node in queue:
                min_val = float('inf')
                min_node = None
                row, col, dist = node

                if valid(row+1, col) and forest[row+1][col] < min_val:
                    min_val = forest[row+1][col]
                    min_node = [row+1, col, dist+1]

                if valid(row-1, col) and forest[row-1][col] < min_val:
                    min_val = forest[row-1][col]
                    min_node = [row-1, col, dist+1]

                if valid(row, col-1) and forest[row][col-1] < min_val:
                    min_val = forest[row][col-1]
                    min_node = [row, col-1, dist+1]

                if valid(row, col+1) and forest[row][col+1] < min_val:
                    min_val = forest[row][col+1]
                    min_node = [row, col+1, dist+1]

                if min_node is None:
                    break

                if not visited[min_node[0]][min_node[1]]:
                    visited[min_node[0]][min_node[1]] = True
                    queue.append(min_node)
                    forest[min_node[0]][min_node[1]] = 1
            return dist

        res = bfs([0, 0, 0])
        forest[0][0] = 1
        # print(forest)
        # print(visited)
        for row in range(row_len):
            for col in range(col_len):
                if forest[row][col] > 1:
                    return -1
        return res

        # print(bfs([0, 0, 0]))

        # @lc code=end
