#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        mini = min(strs)
        maxi = max(strs)
        for i in range(len(mini)):
            if mini[i] != maxi[i]:
                return mini[:i]
        return mini        
# @lc code=end

