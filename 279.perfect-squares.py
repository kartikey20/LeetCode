# @before-stub-for-debug-begin
# @before-stub-for-debug-end

# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**1/2))][::-1]

        for i, _ in enumerate(squares):
            if squares[i] > n:
                squares.pop(i)

        print(squares)

        if n in squares:
            return n

        l = len(squares)

        c = [float('inf')]

        def dfs(num, count):
            count += 1
            if num < n:
                print(l)
                for i in range(l):
                    dfs(num + squares[i], count[:])
            if num == n:
                c[0] = min(c[0], count)
        dfs(0, 0)
        print(c)

# @lc code=end
