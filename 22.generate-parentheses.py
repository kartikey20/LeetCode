#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from copy import deepcopy
# @lc code=start


class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(open, close, path):
            if open > close or open < 0 or close < 0:
                return

            if open == 0 and close == 0:
                res.append(deepcopy(path))
                return

            dfs(open-1, close, path + "(")
            dfs(open, close-1, path + ")")
        dfs(n, n, "")
        return res


# @lc code=end
