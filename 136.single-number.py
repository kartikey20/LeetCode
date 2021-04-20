#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {n : 0 for n in nums}
        for n in nums:
            count[n] += 1
        for key, value in count.items():
            if value == 1:
                return key
        
# @lc code=end

