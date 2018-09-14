class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums) * len(nums[0]):
            return nums
        tempList = []
        for i in range(len(nums)):
            tempList = tempList + nums[i]
        rlist = []
        for j in range(0, len(tempList)-c+1, c):
            inlist = tempList[j:j+c]
            rlist.append(inlist)
        return rlist