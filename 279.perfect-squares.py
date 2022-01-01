# @before-stub-for-debug-begin
# @before-stub-for-debug-end

# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import ceil, floor, sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        n_sqrt = sqrt(n)
        if ceil(n_sqrt) == floor(n_sqrt):
            return 1
        else:
            perfect_squares = [i*i for i in range(1, int(n_sqrt)+1)][::-1]

            def bfs(num):
                count = 0
                queue = [[num, count]]
                for x in queue:
                    for v in perfect_squares:
                        num = x[0] + v
                        count = x[1] + 1
                        queue.append([num, count])
                        if num == n:
                            return count
            return bfs(0)

#   Time Complexity = O(n)
#   Space Complexity = O(n)
# @lc code=end
