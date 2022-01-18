#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get non increasing suffix array
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i <= 0:
            return False

        # find successor to pivot
        j = len(nums) - 1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]

        # reverse suffix array
        nums[i:] = nums[len(nums)-1: i-1: -1]
        return True


# @lc code=end
