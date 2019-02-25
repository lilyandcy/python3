# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        if root == None:
            return res
        queue = []
        queue.append(root)
        while len(queue) != 0:
            count = len(queue)
            temp = []
            while count > 0:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                count -= 1
            res.append(temp)
        return res