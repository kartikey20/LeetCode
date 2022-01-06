#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [set() for _ in range(n+1)]
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if row != col:
                    graph[row+1].add(col+1)
                    graph[col+1].add(row+1)

        print(graph)


# @lc code=end
