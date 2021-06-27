# @before-stub-for-debug-begin
from python3problem35 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return mid
            return low
        return binarySearch(nums,target)
            
            


        
# @lc code=end

