# @before-stub-for-debug-begin
from python3problem389 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
from typing import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in s:
            t = t.replace(i, "", 1)
        return t

# @lc code=end
