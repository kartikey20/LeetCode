#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0] == "-":
            return False
        arr = [int(i) for i in str(x)]
        return True if arr == arr[::-1] else False
        
# @lc code=end

