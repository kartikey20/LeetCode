# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# from operator import imod
from typing import List
# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i+1][0], intervals[i][0])
                intervals[i+1][1] = max(intervals[i+1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals

        # @lc code=end
