#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
from collections import defaultdict
# @lc code=start


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = defaultdict(list)
        sums = 0
        prefix_sum[0] = [-1]
        n = len(nums)
        for i in range(n):
            sums += nums[i]
            start_lst = prefix_sum[sums-k]
            for x in start_lst:
                if sum(nums[x+1:i+1]) % k == 0:
                    count += 1
            start_list2 = prefix_sum[sums]
            start_list2.append(i)
            prefix_sum = start_list2
        return count


# @lc code=end
