#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False for _ in range(n)]

        def bfs(start):
            queue = [start]
            visited[start] = True
            for node in queue:
                if node == end:
                    return True
                for child in graph[node]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append(child)
            return False
        return bfs(start)
# @lc code=end
