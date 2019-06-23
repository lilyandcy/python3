# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root