#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        for w  in range(len(height) - 1,0,-1):
            if height[l] < height[r]:
                res = max(res, height[l] * w)
                l += 1
            else:
                res = max(res,height[r] * w)
                r -= 1
        return res


            # @lc code=end

