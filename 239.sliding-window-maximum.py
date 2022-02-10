#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        res = []
        # print(n-k)
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
            # print(w)
        return res

# @lc code=end
