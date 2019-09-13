class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        s  = 0
        for num in A:
            s = s*2 + num
            res.append(s%5==0)
        return res