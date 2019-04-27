# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        s = []
        dummy = TreeNode(0)
        p = dummy
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                cur = s.pop()
                root = cur.right
                cur.left = None
                p.right = cur
                p = p.right

        return dummy.right