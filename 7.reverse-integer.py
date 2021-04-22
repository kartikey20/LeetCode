# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        numStr = str(x)
        sign = 1
        if numStr[0] == '-':
            sign = -1
            numStr = numStr.replace('-','')
        return sign * int(numStr[::-1]) if -2**31 <= sign * int(numStr[::-1]) <= 2**31 -1 else 0
# @lc code=end

