# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        sArr = []
        mArr = []
        cur = head
        while cur != None:
            if cur.val not in mArr:
                if cur.val not in sArr:
                    sArr.append(cur.val)
                else:
                    mArr.append(cur.val)
                    sArr.remove(cur.val)
            cur = cur.next
        cur = head
        tempCur = head
        if sArr == []:
            return None
        while cur != None:
            if cur.val in sArr:
                tempCur = cur
                cur = cur.next
            else:
                tempCur.next = cur.next
                cur = cur.next
        if head.val in mArr:
            head = head.next
        return head
