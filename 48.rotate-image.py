#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(list(zip(*matrix[::-1])))
        matrix[:] = zip(*matrix[::-1])
        # print(w)

# @lc code=end
