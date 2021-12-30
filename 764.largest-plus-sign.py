# @before-stub-for-debug-begin
from python3problem764 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=764 lang=python3
#
# [764] Largest Plus Sign
#

# @lc code=start


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        row_len = len(mines)
        col_len = len(mines[0])
        largest_plus_sign = 0

        def valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and not mines[row][col] == 0

        def expand(row, col):
            count = 0
            while valid(row, col-count-1) and valid(row, col+count+1) and valid(row+count+1, col) and valid(row-count-1, col):
                count += 1
            return count

        for row in range(row_len):
            for col in range(col_len):
                if valid(row, col):
                    largest_plus_sign = max(largest_plus_sign, expand(row, col))
        return largest_plus_sign

        # @lc code=end
