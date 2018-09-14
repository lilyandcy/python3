# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head
        length = 0
        h = head
        d = {}
        while h:
            length = length + 1
            d[length] = h
            h = h.next
        return d[length//2+1]