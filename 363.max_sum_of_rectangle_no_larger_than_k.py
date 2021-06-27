# @before-stub-for-debug-begin
from python3problem363 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# @lc code=start


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = -float('inf')

        def get_all_sub_mat(mat):
            rows = len(mat)
            cols = len(mat[0])

            def ContinSubSeq(lst):
                size = len(lst)
                for start in range(size):
                    for end in range(start + 1, size + 1):
                        yield (start, end)

            for start_row, end_row in ContinSubSeq(list(range(rows))):
                for start_col, end_col in ContinSubSeq(list(range(cols))):
                    yield [i[start_col:end_col] for i in mat[start_row:end_row]]

        for x in get_all_sub_mat(matrix):
            sumArr = sum(list(map(sum, x)))
            if sumArr <= k:
                res = max(res, sumArr)
        return res

        # @lc code=end
