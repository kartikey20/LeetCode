#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I' : 1,
            'IV': 4,
            'V' : 5,
            'IX' : 9,
            'X' : 10,
            'LX' : 40,
            'L' : 50,
            'XC' : 90,
            'C' : 100,
            'CD': 400,
            'D' : 500,
            'CM' : 900,
            'M' : 1000
            }
        
# @lc code=end

