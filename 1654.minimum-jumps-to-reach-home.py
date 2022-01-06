#
# @lc app=leetcode id=1654 lang=python3
#
# [1654] Minimum Jumps to Reach Home
#
from typing import List
# @lc code=start


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)

        def bfs(start):
            queue = [[start, 0, False]]
            for x in queue:
                node, count, backward = x
                if node == x:
                    return count
                bak
                if not backward and (node-b) not in forbidden_set:
                    queue.append([node-b, count + 1, True])
                if (node+a) not in forbidden_set:
                    queue.append([node+a, count + 1, False])
        print(bfs(0))


A = Solution()
A.minimumJumps([14, 4, 18, 1, 15], 3, 15, 9)

# @lc code=end
