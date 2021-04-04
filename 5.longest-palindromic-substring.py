# @before-stub-for-debug-begin
from python3problem5 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def dfs(substr,index):
            if substr[::-1] == substr:
                return substr
            index -= 1
            substr = s[:index]
            dfs(substr, index)
        return dfs(s, len(s))

        
# @lc code=end

