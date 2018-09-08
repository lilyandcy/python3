class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list = [0]
        list = list * (len(nums) + 1)
        print (list)
        for num in nums:
            list[num] = 1
        return list.index(0)