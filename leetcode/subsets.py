class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for num in nums:
            nres=res.copy()
            for nre in nres:
                res.append([num]+nre)
        return res