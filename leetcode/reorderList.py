# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return
        cur = head
        l = []
        while cur != None:
            l.append(cur.val)
            cur = cur.next
        templ = l.copy()
        templ.reverse()
        res = []
        for i in range(len(l)//2):
            res.append(l[i])
            res.append(templ[i])
        if len(l) % 2 != 0:
            res.append(l[len(l)//2])
        cur = head
        i = 0
        while cur != None:
            cur.val = res[i]
            i += 1
            cur = cur.next