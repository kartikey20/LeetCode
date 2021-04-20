#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        for key, value in count.items():
            if value > len(nums) // 2:
                return key
        
# @lc code=end

