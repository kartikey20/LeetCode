#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from bisect import bisect_left
# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = bisect_left(numbers, target - numbers[i])
            if 0 <= j < len(numbers) and numbers[j] == target - numbers[i]:
                return [i + 1, j + 1]
# @lc code=end
