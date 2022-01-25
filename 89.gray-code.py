#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
from itertools import permutations
# @lc code=start


class Solution:
    def grayCode(self, n: int) -> List[int]:
        def gray_seq(arr):
            for i in range(len(arr)-1):
                first = sum([int(x) for x in bin(arr[i])[2:]])
                second = sum([int(x) for x in bin(arr[i+1])[2:]])
                if abs(first - second) == 1:
                    continue
                else:
                    return False
            return True

        seq = list(range(2**n))
        for x in permutations(seq, len(seq)):
            if gray_seq(x):
                return list(x)

            # @lc code=end
