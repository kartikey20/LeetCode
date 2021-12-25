# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=854 lang=python3
#
# [854] K-Similar Strings
#
from itertools import permutations
# @lc code=start


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        count = 0
        for x in permutations(s1, len(s1)):
            if "".join(x) == s2:
                return count
            count += 1


# @lc code=end
