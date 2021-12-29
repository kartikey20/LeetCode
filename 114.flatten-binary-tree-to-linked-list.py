# @before-stub-for-debug-begin
from python3problem114 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        print(root.val)

        def dfs(root):
            if root.left:
                res.extend([root.left.val, None])
                dfs(root.left)

            if root.right:
                res.extend([root.right.val, None])
                dfs(root.right)
        if root:
            res.extend((root.val, None))
            dfs(root)
        return res[:-1]
# @lc code=end
