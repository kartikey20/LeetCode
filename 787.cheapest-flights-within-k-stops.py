# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for i in range(n):
            graph[flights[i][0]].append([flights[i][1], flights[i][2]])

        print(graph)

        def bfs(start):
            queue = [start]
            min_cost = float('inf')
            for node in queue:
                for child in graph[node[0]]:
                    cost = node[1] + child[1]
                    count = node[2] + 1
                    if count <= k:
                        queue.append([child[0], cost, count])
                    if child[0] == dst:
                        min_cost = min(min_cost, cost)
            print(queue)
            return min_cost
        res = bfs([src, 0, 0])
        return res if not res == float('inf') else -1


# @lc code=end
