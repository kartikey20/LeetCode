# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 3:
            if n == 1:
                return s
            elif n == 2:
                return s if s == s[::-1] else s[0]
        new_str = ''
        i = 0
        while i < n:
            new_str += s[i]
            i += 1
            if i < n:
                new_str += '#'
        max_len = 0
        res = ''
        new_n = len(new_str)
        for i in range(1, new_n):
            sub_str = ''
            l = i - 1
            r = i + 1
            while l >= 0 and r < new_n and new_str[l] == new_str[r]:
                if new_str[l] != '#':
                    sub_str = new_str[l:r+1]
                l -= 1
                r += 1
            if len(sub_str) > max_len:
                res = sub_str
                max_len = len(sub_str)
        ans = res.replace('#', '')
        if len(ans) == 0:
            return s[0]
        else:
            return ans

# @lc code=end
