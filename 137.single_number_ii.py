#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
from collections import Counter

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for x in nums:
            if count[x] == 1:
                return x
# @lc code=end
