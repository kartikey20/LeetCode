#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from bisect import bisect_left
# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            i = bisect_left(row, target)
            if 0 <= i < len(row) and row[i] == target:
                return True
        return False
        # @lc code=end
