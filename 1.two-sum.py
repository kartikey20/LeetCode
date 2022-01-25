#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from bisect import bisect_left
from copy import deepcopy
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_array = deepcopy(nums)
            new_array[i] = float('-inf')
            b = bisect_left(new_array, target-nums[i])
            if 0 <= b < len(nums) and nums[b] == target-nums[i]:
                return [i, b]


# @lc code=end
