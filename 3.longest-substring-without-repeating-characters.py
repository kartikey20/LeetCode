#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0
        for i, right in enumerate(s):
            while right in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(right)
            res = max(res, i - left + 1)
        return res


# @lc code=end
