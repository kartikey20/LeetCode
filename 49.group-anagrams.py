#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import Counter
from itertools import groupby
from collections import OrderedDict
# @lc code=start


# class OrderedCounter(Counter, OrderedDict):
#     def __repr__(self):
#         return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=sorted)
        return sorted([sorted(list(g)) for _, g in groupby(strs, key=lambda x: sorted(Counter(x).items()))], key=len)
        # for k, g in groupby(strs, lambda x: x):
        #     print(k, list(g))

# @lc code=end
