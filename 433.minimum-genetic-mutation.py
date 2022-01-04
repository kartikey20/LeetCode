# @before-stub-for-debug-begin
from python3problem433 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankSet = set(bank)

        def bfs(start):
            queue = [[start, 0]]
            for elem in queue:
                node, step = elem
                if node == end:
                    return step
                for i in range(len(node)):
                    for c in 'AGCT':
                        mutation = node[:i] + c + node[i+1:]
                        if mutation in bankSet:
                            bankSet.remove(mutation)
                            queue.append([mutation, step+1])
        ans = bfs(start)
        return ans if ans is not None else -1


# @lc code=end
