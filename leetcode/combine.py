import itertools
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(n):
            nums.append(i+1)
        res = []
        for i in itertools.combinations(nums, k):
            res.append(i)
        return res