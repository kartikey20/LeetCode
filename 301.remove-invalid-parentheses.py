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
        valid = set()

        if is_valid(s):
            return [s]
        else:
            for i in range(len(s)):
                substr = s[:i] + s[i+1:]
                if is_valid(substr):
                    # print(substr)
                    valid.add(substr)
        ans = list(valid)
        if len(ans) != 0:
            return ans
        else:
            return [""]

        # @lc code=end
