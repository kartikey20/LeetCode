#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#
from itertools import groupby
# @lc code=start
from collections import defaultdict

from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know = set()
        know.add(0)
        know.add(firstPerson)

        s = sorted(meetings, key=lambda x: x[2])
        for time, group in groupby(s, key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(set)
            for x, y, _ in group:
                graph[x].add(y)
                graph[y].add(x)
                if x in know:
                    queue.add(x)
                if y in know:
                    queue.add(y)

            queue = list(queue)
            for x in queue:
                for child in graph[x]:
                    if child not in know:
                        know.add(child)
                        queue.append(child)
        return list(know)


A = Solution()
A.findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1)
# @lc code=end
