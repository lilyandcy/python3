# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        lenA = 1

        hA = headA
        while hA.next != None:
            lenA += 1
            hA = hA.next

        lenB = 1
        hB = headB
        while hB.next != None:
            lenB += 1
            hB = hB.next

        if hA != hB:
            return None

        hA = headA
        hB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                hA = hA.next
        else:
            for i in range(lenB - lenA):
                hB = hB.next

        while hA != hB:
            hA = hA.next
            hB = hB.next

        return hA
