# @before-stub-for-debug-begin
from python3problem239 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
[5, 1, -1, 2, 5, 3, 6, 7]

https: // leetcode.com/problems/maximum-subarray/submissions/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # arr = nums[:k]
        # res.append(max(arr))
        # for i in range(k, len(nums)):
        #     arr.pop(0)
        #     arr.append(nums[i])
        #     res.append(max(arr))
        # return res

        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

# @lc code=end
