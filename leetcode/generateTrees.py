# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(tree):
            ans = []
            for i, val in enumerate(tree):
                left, right = tree[:i], tree[i+1:]
                for ltree in helper(left) or [None]:
                    for rtree in helper(right) or [None]:
                        root = TreeNode(val)
                        root.left, root.right = ltree, rtree
                        ans.append(root)
            return ans
        return helper(range(1, n+1))