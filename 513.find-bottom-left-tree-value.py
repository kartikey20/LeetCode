# @before-stub-for-debug-begin
from python3problem513 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        layers = []
        queue = [root]
        while queue:
            curr_layer = []
            layers.append(queue[:])
            node = queue.pop(0)
            if node.left:
                curr_layer.append(node.left)
            if node.right:
                curr_layer.append(node.right)
            queue = curr_layer
        lastnode = layers[-1][0]
        return lastnode.val
        # if lastnode.left:
        #     return lastnode.left.val
        # else:
        #     return lastnode.right.val


# @lc code=end
