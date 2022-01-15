# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# @lc code=start
from collections import defaultdict


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = []
        prefix_sum = defaultdict(set)
        prefix_sum[0].add(-1)
        sums = 0
        min_len = float('inf')
        n = len(nums)
        for i in range(n):
            sums += nums[i]
            for key in list(prefix_sum):
                start_index = prefix_sum[sums - (target+key)]
                for x in start_index:
                    res.append([x+1, i])
                start_index = prefix_sum[sums]
                start_index.add(i)
                prefix_sum[sums] = start_index
        print(res)
        for left, right in res:
            min_len = min(min_len, right-left+1)
        return min_len


# @lc code=end
