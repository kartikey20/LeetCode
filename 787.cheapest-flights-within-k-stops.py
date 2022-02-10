# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start


from heapq import heappop, heappush
import queue


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(3)]
        for u, v, price in flights:
            graph[u].append((v, price))

        cost = [float('inf') for _ in range(3)]

        def dijkstra(start, graph):
            queue = [(start, 0, -1)]
            cost[start] = 0
            while queue:
                parent, parent_cost, steps = heappop(queue)
                if parent_cost == cost[parent]:
                    for child, child_cost in graph[parent]:
                        if child_cost+parent_cost < cost[child] and steps < k:
                            child[cost] = child_cost + parent_cost
                            heappush(queue, (child, cost[child], steps+1))
        dijkstra(src)


# @lc code=end
