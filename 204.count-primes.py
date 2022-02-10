#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
from collections import defaultdict
# from this import s
# @lc code=start


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(n):
            for d in range(2, int(i**1/2)+1):
                if i % d == 0:
                    break
            count += 1
        return count

        # @lc code=end
