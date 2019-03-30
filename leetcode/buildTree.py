# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        res = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        res.left = self.buildTree(preorder[1:index+1], inorder[:index])
        res.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return res