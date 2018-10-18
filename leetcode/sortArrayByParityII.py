class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddL = []
        evenL = []
        res = []
        for num in A:
            if num % 2 == 0:
                evenL.append(num)
            else:
                oddL.append(num)
        for i in range(len(evenL)):
            res.append(evenL[i])
            res.append(oddL[i])
        return res