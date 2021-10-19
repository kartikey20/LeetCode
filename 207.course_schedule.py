# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for x in prerequisites:
            preMap[x[0]].append([x[1]])
        g = collections.defaultdict(list, preMap)

        def toposort(graph):
            res, found = [], [0] * len(graph)
            stack = list(range(len(graph)))
            while stack:
                node = stack.pop()
                if node < 0:
                    res.append(~node)
                elif not found[node]:
                    found += 1
                    stack.append(~node)
                    stack += graph[node]
            for node in res:
                if any(found[nei] for nei in graph[node]):
                    return False
            return True
        return toposort(g)


a = Solution()
b = a.canFinish(2, [1, 0])
print(b)
# @lc code=end
