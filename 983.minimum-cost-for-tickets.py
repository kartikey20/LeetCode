#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # [1, 4, 6, 7, 8, 9, 10, 11, 13,  15, 17, 28, 32, 33 ,34, 35]
        # [     7     -       7         -  1   1 -         7        ] = 23
        # [                      15                 -        7      ] = 22
        def nextMultiple(n, k):
            return n + (k - n % k)

        def dfs(arr, index):
            


# @lc code=end

