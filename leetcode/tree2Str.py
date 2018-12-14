class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""
        if t.left == None and t.right == None:
            return str(t.val)
        elif t.left == None:
            return str(t.val) + "()" + "(" + self.tree2str(t.right) + ")"
        elif t.right == None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        else:
            return str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"