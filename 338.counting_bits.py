# @before-stub-for-debug-begin
from python3problem338 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from collections import Counter


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(0, num+1):
            count = Counter(bin(i))
            for key, value in count.items():
                if key == '1':
                    res.append(value)
        return res


# @lc code=end
