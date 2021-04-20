#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < val:
                l += 1
            elif nums[r] > val:
                r -=1
            else:
                nums.remove(val)
                l += 1
        return len(nums)
        
# @lc code=end

