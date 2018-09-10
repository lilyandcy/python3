class Solution:
    def findPairs2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rnum = 0
        numsdict = {}
        if k != 0:
            nums = list(set(nums))
            nums.sort()
            for i in range(len(nums)):
                numsdict[nums[i]+k] = nums[i]
                if nums[i] in numsdict.keys():
                    rnum = rnum + 1
            return rnum
        else:
            nums1 = list(set(nums))
            for num in nums1:
                if nums.count(num) > 1:
                    rnum = rnum + 1
            return rnum