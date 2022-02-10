#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from typing import List
from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        def dijkstra(start, graph):
            visited = set()
            max_heap = [(start, -1)]
            while max_heap:
                curr, prob = heappop(max_heap)
                visited.add(curr)
                if curr == end:
                    return -prob
                for child, child_prob in graph[curr]:
                    if child not in visited:
                        new_prob = -1 * abs(prob * child_prob)
                        heappush(max_heap, (child, new_prob))
        res = dijkstra(start, graph)
        return res if res is not None else 0


#         # print(probability)
# A = Solution()
# A.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2)
# @lc code=end
