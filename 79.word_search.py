#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

[1,2,3,4,10]
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(val):
            val += 1
            if val == 10:
                return
        dfs(0)

        
        

        
# @lc code=end