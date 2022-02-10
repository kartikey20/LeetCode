#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

# @lc code=start
from heapq import heappop, heappush


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append([v, weight])
            graph[v].append([v, weight])

        dist = [float('inf') for _ in range(3)]

        def dijkstra(start, graph):
            queue = [(start, 0)]
            dist[start] = 0
            while queue:
                parent, parent_dist = heappop(queue)
                if parent_dist == dist[parent]:
                    for child, child_dist in graph[parent]:
                        if child_dist + parent_dist < dist[child]:
                            dist[child] = child_dist + parent_dist
                            heappush(queue, (child, dist[child]))
        dijkstra(0, graph)


# @lc code=end
