# @before-stub-for-debug-begin
from python3problem53 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
import itertools


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = 0
        for i in combinations(nums, len(nums)):
            maxi = max(maxi, sum(i))
        return maxi

    # @lc code=end
