#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            queue = [root]
            layers = []
            while queue:
                curr_layer = []
                layers.append(queue)
                for x in queue:
                    if x.left:
                        curr_layer.append(x.left)
                    if x.right:
                        curr_layer.append(x.right)

                queue = curr_layer

            for x in layers:
                for i in range(len(x)-1):
                    x[i].next = x[i+1]
            return root
        else:
            return root
# @lc code=end
