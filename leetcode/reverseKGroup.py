# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        linkList = []
        cur = head
        while cur != None:
            linkList.append(cur.val)
            cur = cur.next
        l = len(linkList)
        m = l % k
        i = 0
        while i < l - m:
            tempList = linkList[i:i+k]
            tempList.reverse()
            linkList[i:i+k] = tempList
            i = i + k
        cur = head
        for i in range(l):
            cur.val = linkList[i]
            cur = cur.next
        return head