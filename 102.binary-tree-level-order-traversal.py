#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [[root.val]]

        def bfs(node):
            res = []
            if not node.left == None:
                res.append(node.left.val)
            if not node.right == None:
                res.append(node.right.val)
            if not len(res) == 0:
                queue.append(res)
            if not node.left == None:
                bfs(node.left)
            if not node.right == None:
                bfs(node.right)

        return queue

# @lc code=end
