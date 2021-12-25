#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from collections import defaultdict
# @lc code=start


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        sums = 0
        for i in range(n):
            sums += nums[i]
            count += prefix_sum[sums - k]
            prefix_sum[sums] += 1
        return count

# @lc code=end
