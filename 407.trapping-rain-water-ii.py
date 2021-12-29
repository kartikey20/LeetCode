# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
class Solution:
    def trapRainWater(self, height):
        row_len = len(height)
        col_len = len(height[0])
        count = [0]
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        def valid(row, col, prev_row, prev_col):
            if row > 0 and col > 0 and row < row_len-1 and \
                col < col_len-1 and not visited[row][col] \
                    and height[row][col] <= height[prev_row][prev_col]:
                return True

            return False

        def bfs(start):
            visited[start[0]][start[1]] = True
            queue = [start]

            for node in queue:
                row, col = node
                if valid(row+1, col, row, col):
                    visited[row+1][col] = True
                    count[0] += 1
                    queue.append([row+1, col])

                if valid(row-1, col, row, col):
                    visited[row-1][col] = True
                    count[0] += 1
                    queue.append([row-1, col])

                if valid(row, col+1, row, col):
                    visited[row][col+1] = True
                    count[0] += 1
                    queue.append([row, col+1])

                if valid(row, col-1, row, col):
                    visited[row][col-1] = True
                    count[0] += 1
                    queue.append([row, col-1])

        for row in range(row_len):
            for col in range(col_len):
                if row > 0 and col > 0 and row < row_len-1 and \
                        col < col_len-1 and not visited[row][col]:
                    bfs([row, col])

        print(visited)
        return count[0]


# @lc code=end
