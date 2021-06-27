#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
s = "abc", t = "ahbgdc"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        j = 0
        for i in s:
            while(j < len(t)):
                if i == t[j]:
                    c += 1
                    j += 1
                    break
                j += 1
        if c == len(s):
            return True
        else:
            return False

# @lc code=end
