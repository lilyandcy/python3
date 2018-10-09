class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            bini = bin(i)
            res.append(bini.count("1"))
        return res