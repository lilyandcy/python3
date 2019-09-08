from itertools import combinations

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for comb in combinations(nums, 3):
           if comb[0] + comb[1] > comb[2]:
                res += 1
        return res