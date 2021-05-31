#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
from collections import Counter
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                res.append(k)
        return res


        
# @lc code=end

