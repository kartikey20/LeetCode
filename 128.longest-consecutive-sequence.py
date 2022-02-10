#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = defaultdict(int)
        for num in nums:
            parent[num] = num

        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                parent[b] = a

        for num in nums:
            if num-1 in nums:
                union(num-1, num)
            if num+1 in nums:
                union(num+1, num)


# @lc code=end
