# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        p = TreeNode(max(nums))
        index = nums.index(max(nums))
        p.left = self.constructMaximumBinaryTree(nums[:index])
        p.right = self.constructMaximumBinaryTree(nums[index+1:])
        return p