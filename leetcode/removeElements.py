# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prenode = ListNode(None)
        prenode.next = head
        q = prenode
        p = q.next
        while p:
            if p.val == val:
                q.next = p.next
                p = p.next
            else:
                q = q.next
                p = p.next
        return prenode.next
