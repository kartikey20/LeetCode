# @before-stub-for-debug-begin
from itertools import count
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# @lc code=start
# 0


# def recursion_factorial(a):

# if a == 1:
#         return 1
#     else:
#         return (1 + recursion_factorial(a-1) + recursion_factorial(a-2))


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


# It's basically the Fibonacci Sequence... of course you wouldn't know that just by reading the problem.

# What clue's algorithm is doing is basically this:
# For any given step n, you can reach it from 2 steps away(n-2) or 1 step away(n-1).
# Therefore, the total number of ways to get to n is the sum of the total number of ways to get to(n-2) and the total number of ways to get to(n-1)

# Although not clearly evident in his/her algorithm, 'a' represents(n-2) and 'b' represents the(n-1)
# @lc code=end
