class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evenlist = []
        oddlist = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                evenlist.append(A[i])
            else:
                oddlist.append(A[i])
        return evenlist + oddlist