class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bnum = bin(num)[2:]
        lennum = len(bnum)
        rbnum = ""
        for i in range(lennum):
            rbnum = rbnum + str((1 - int(bnum[i])))
        return int(rbnum, 2)