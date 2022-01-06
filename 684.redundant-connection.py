#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from collections import defaultdict
# @lc code=start


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = defaultdict(int)

        def make_set(v):
            parent[v] = v

        for u, v in edges:
            make_set(u)
            make_set(v)

        def find(v):
            if v == parent[v]:
                return v
            return find(parent[v])

        def union(u, v):
            a = find(u)
            b = find(v)
            if a != b:
                parent[b] = a

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            union(u, v)

# @lc code=end
