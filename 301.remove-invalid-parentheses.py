# @before-stub-for-debug-begin
# @before-stub-for-debug-end
#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        level = {s}

        while True:
            valid = filter(is_valid, level)
            if list(valid):
                return list(valid)
            new_level = {}
            for s in level:
                for i in range(len(s)):
                    new_level.add(s[:i] + s[i+1:])
            level = new_level

        # @lc code=end
