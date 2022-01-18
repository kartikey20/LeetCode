# @before-stub-for-debug-begin

# @before-stub-for-debug-end
from typing import List
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# @lc code=start
import re
from copy import deepcopy


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = [False] * len(wordDict)
        res = [False]

        def dfs(string, visited):
            if len(string) == 0:
                res[0] = True
            else:
                for i, v in enumerate(wordDict):
                    if not visited[i]:
                        new_visited = deepcopy(visited)
                        new_visited[i] = True
                        new_string = re.sub(f'^{v}|{v}$', '', string)
                        # print(string)
                        dfs(deepcopy(new_string), new_visited)

        dfs(s, visited[:])
        return res[0]

        # @lc code=end
