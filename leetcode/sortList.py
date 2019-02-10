# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        cur = head
        templist =[]
        while cur != None:
            templist.append(cur.val)
            cur = cur.next
        templist.sort()
        cur = head
        i = 0
        while cur != None:
            cur.val = templist[i]
            i += 1
            cur = cur.next
        return head