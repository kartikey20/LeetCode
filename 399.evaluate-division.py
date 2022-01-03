#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from collections import defaultdict
# @lc code=start

from copy import deepcopy


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            u, v = equations[i]
            graph[u].append([v, values[i]])
            graph[v].append([u, 1/values[i]])

        visited = {node: False for node in graph}

        res = []

        def bfs(start, end, visited):
            queue = [[start, 1]]
            visited[start] = True
            for x in queue:
                node, prod = x
                for child in graph[node]:
                    if not visited[child[0]]:
                        visited[child[0]] = True
                        queue.append([child[0], prod * child[1]])
                if node == end:
                    return prod

        for query in queries:
            if not query[0] in visited or not query[1] in visited:
                res.append(-1)
            else:
                val = bfs(query[0], query[1], deepcopy(visited))
                res.append(val if val is not None else -1)
        return res
# @lc code=end
