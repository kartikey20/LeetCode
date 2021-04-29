# @before-stub-for-debug-begin
from python3problem58 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        if len(l) == 0:
            return 0
        else:
            return len(l[-1])

# @lc code=end
