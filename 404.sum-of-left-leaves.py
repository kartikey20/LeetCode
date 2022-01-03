#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def bfs(start):
            queue = [[start, 0]]
            res = 0
            for x in queue:
                node, direction = x
                if node.left:
                    queue.append([node.left, -1])
                if node.right:
                    queue.append([node.right, 1])
                if node.left is None and node.right is None and direction == -1:
                    res += node.val

            return res
        return bfs(root)


# @lc code=end
