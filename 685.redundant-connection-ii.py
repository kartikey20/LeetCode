#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
from collections import defaultdict
# @lc code=start


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = defaultdict(int)

        def make_set(v):
            parent[v] = v

        for u, v in edges:
            print(u, v)
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
        res = []
        for u, v in edges:
            if find(u) == find(v):
                res.append([u, v])
                # return [u, v]
            union(u, v)
        print(res)

# @lc code=end
