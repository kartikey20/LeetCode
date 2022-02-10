#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import defaultdict
from email.policy import default


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        parent = defaultdict(int)
        for i in range(len(graph)):
            parent[i] = i

        def find(v):
            if parent[v] == v:
                return v
            return find(parent[v])

        for i in range(len(graph)):
            for child in graph[i]:
                if find(i) == find(child):
                    return False
                union()


# @lc code=end
