# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # move next node's val to fill in the node you want to delete
        # del the next node, which is a very easy operation in single linked list
        node.val = node.next.val
        node.next = node.next.next