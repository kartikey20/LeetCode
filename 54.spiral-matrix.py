# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            print(*matrix)
            matrix = [*zip(*matrix)][::-1]
        return res

        # @lc code=end
