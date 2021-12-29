#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        layers = []
        queue = [root]
        while queue:
            curr_layer = []

            layers.append(queue)
            node = queue.pop(0)
            if node.left:
                curr_layer.append(node.left)
            if node.right:
                curr_layer.append(node.right)
            if node.left and node.right:
                max_node = max(node.left.val, node.left.val)
                res.append(max_node)
            else:
                if node.left:
                    res.append(node.left.val)
                else:
                    res.append()
            queue = curr_layer
        print(res)


# @lc code=end
