#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
import itertools
# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(0, len(nums) + 1):
            for x in itertools.combinations(nums, i):
                res.append(list(x))
        return res

# @lc code=end
