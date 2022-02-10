#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
from heapq import heappop, heappush
from collections import defaultdict
import queue
# @lc code=start


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append([v, t])

        time_taken = defaultdict(lambda: float('inf'))

        def dijkstra(start, graph):
            queue = [(start, 0)]
            time_taken[start] = 0
            while queue:
                parent, parent_time = heappop(queue)
                if parent_time == time_taken[parent]:
                    for child, child_time in graph[parent]:
                        if child_time + parent_time < time_taken[child]:
                            time_taken[child] = child_time + parent_time
                            heappush(queue, (child, time_taken[child]))
        dijkstra(k, graph)
        print(graph)
        print(time
        _time_taken=list(time_taken.values())
        if len(_time_taken) == 1:
            return _time_taken
        if all(_time_taken[1:]):
            return max(_time_taken)
        else:
            return -1

# @lc code=end
