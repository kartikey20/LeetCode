#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#
from collections import defaultdict
# @lc code=start
from copy import deepcopy


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        visited = [False for _ in range(n)]

        dic = defaultdict(set)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(i+1, n):
                x2, y2, r2 = bombs[j]
                sq_dist = pow(x1-x2, 2) + pow(y1 - y2, 2)
                if sq_dist <= pow(r1, 2):
                    dic[i].add(j)
                if sq_dist <= pow(r2, 2):
                    dic[j].add(i)
        print(dic)

        def bfs(start, visited):
            detonations = 0
            queue = [[start, 0]]
            visited[start] = True
            for x in queue:
                node, count = x
                detonations = max(detonations, count)
                for child in dic[node]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append([child, count + 1])
            return detonations

        max_detonations = 0
        for i in range(len(bombs)):
            max_detonations = max(max_detonations, bfs(i, deepcopy(visited)))
        return max_detonations + 1
        # @lc code=end
