# @before-stub-for-debug-begin
from python3problem190 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start


class Solution:
    def reverseBits(self, n: int) -> int:
        oribin = '{0:032b}'.format(n)
        reversebin = oribin[::-1]
        return int(reversebin, 2)

# @lc code=end
