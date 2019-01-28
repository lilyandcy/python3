# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head
        cur = head
        length = 1
        while cur.next != None:
            cur = cur.next
            length += 1
        loop = length - (k % length)
        tail = cur
        cur.next = head
        cur = head
        for i in range(loop):
            cur = cur.next
            tail = tail.next
        tail.next = None
        return cur