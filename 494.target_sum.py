# @before-stub-for-debug-begin

# @before-stub-for-debug-end

#
# @lc app=leetcode id=494 lang=python3
#
import itertools

# [1, 1, 1, 1, 1] Target = 3
# 5
# 0


class Solution:
    def findTargetSumWays(self, nums, target):
        count = 0
        res = 0

        def dot(arr1, arr2):
            return sum(x*y for x, y in zip(arr1, arr2))

        for x in itertools.product([-1, 1], repeat=len(nums)):
            res = dot(x*nums)

            if sum(res) == target:
                count += 1
        return count


# @lc code=end
