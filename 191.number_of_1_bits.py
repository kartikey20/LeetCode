# @before-stub-for-debug-begin
from python3problem191 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
from typing import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        k = str(n)
        c = Counter(k)
        return c['1']

# @lc code=end
