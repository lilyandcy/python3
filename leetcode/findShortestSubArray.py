class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unit = []
        temp = []
        dim = 0
        start = 0
        end = 0
        length = 0
        numsset = set(nums)
        for num in numsset:
            dim = nums.count(num)
            start = nums.index(num)
            end = len(nums) - nums[::-1].index(num)
            length = end - start
            unit = [dim, length]
            temp.append(unit)
        print(temp)
        maxdim = 0
        shortlen = 50001
        for i in range(len(temp)):
            if maxdim < temp[i][0]:
                       maxdim = temp[i][0]
                       shortlen = temp[i][1]
            else:
                if maxdim == temp[i][0] and shortlen > temp[i][1]:
                    shortlen = temp[i][1]
        return shortlen