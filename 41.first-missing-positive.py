# @before-stub-for-debug-begin
from python3problem41 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        first = 1
        while first in nums:
            first += 1
        return first
        
# @lc code=end

