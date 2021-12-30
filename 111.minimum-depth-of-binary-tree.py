# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(start):
            queue = [start]
            count = 0
            while queue:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.left or node.right:
                    count += 1
            return count

        if root:
            return bfs(root)
        else:
            return 0
        # @lc code=end
