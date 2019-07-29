# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path_num = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return self.path_num
        self.getPathNum(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)

        return self.path_num

    def getPathNum(self, root:TreeNode, sum:int):
        if root == None:
            return
        if root.val == sum:
            self.path_num += 1
        new_sum = sum - root.val
        self.getPathNum(root.left, new_sum)
        self.getPathNum(root.right, new_sum)