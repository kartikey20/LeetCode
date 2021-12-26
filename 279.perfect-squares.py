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
        perfect_squares = [i*i for i in range(1, int(n**1/2) + 1)][::-1]
        squares = list(filter(lambda x: x < n, perfect_squares))

        l = len(squares)

        c = [float('inf')]

        def dfs(num, count):
            if num < n:
                for i in range(l):
                    dfs(num + squares[i], count+1)
            if num == n:
                c[0] = min(c[0], count)
        dfs(0, 0)
        return c[0] if c[0] != float('inf') else n


A = Solution()
print(A.numSquares(45))
# @lc code=end
