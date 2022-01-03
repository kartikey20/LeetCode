# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = coins[::-1]
        n = len(coins)

        def bfs(start):
            count = 0
            queue = [[start, count]]
            for node in queue:
                num = node[0]
                steps = node[1]
                if num < amount:
                    for i in range(n):
                        queue.append([num + coins[i], steps+1])
                if num == amount:
                    return steps
            return count
        count = bfs(0)
        if count == 0:
            return -1
        else:
            return count


# @lc code=end
