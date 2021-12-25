#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []

        def bfs(node):
            if not node.left == None:
                queue.append(node.left.val)
            if not node.right == None:
                queue.append(node.right.val)
            if not node.left == None:
                bfs(node.left)
            if not node.right == None:
                bfs(node.right)
        bfs(root)
        print(queue)


# @lc code=end
