class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        temp = []
        cur = head
        while cur != None:
            temp.append(cur.val)
            cur = cur.next
        tempmn = temp[m-1:n]
        tempmn.reverse()
        temp[m-1:n] = tempmn
        cur = head
        for i in range(len(temp)):
            cur.val = temp[i]
            cur = cur.next
        return head