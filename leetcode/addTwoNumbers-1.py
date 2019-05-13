class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        strL1 = ""
        while l1 != None:
            strL1 += str(l1.val)
            l1 = l1.next
        strL2 = ""
        while l2 != None:
            strL2 += str(l2.val)
            l2 = l2.next
        valL3 = str(int(strL1) + int(strL2))
        l3 = ListNode(0)
        top = l3
        if len(valL3) == 1:
            return ListNode(valL3[0])
        for i in range(len(valL3)-1):
            l3.val = int(valL3[i])
            tmp = ListNode(valL3[i+1])
            l3.next = tmp
            l3 = l3.next
        return top