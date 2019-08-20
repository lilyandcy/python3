# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = [0]
        def tile(node):
            if not node:
                return 0
            left = tile(node.left)
            right = tile(node.right)
            res[0] += abs(left - right)
            return left + right + node.val
        tile(root)
        return res[0]