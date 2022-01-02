# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from typing import List

from copy import deepcopy


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def layers(start, visited):
            visited[start] = True
            queue = [start]
            count = 0
            while queue:
                layer = []
                count += 1
                for node in queue:
                    for child in graph[node]:
                        if not visited[child]:
                            visited[child] = True
                            layer.append(child)
                queue = layer
            return count

        heights = [0] * n
        for i in range(n):
            height = layers(i, visited[:])
            heights[i] = height

        min_height = min(heights)
        return [node for node in range(n) if heights[node] == min_height]

        # @lc code=end
