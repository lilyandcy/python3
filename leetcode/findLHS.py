class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashNum = dict()
        for num in nums:
            if num in hashNum:
                hashNum[num] += 1
            else:
                hashNum[num] = 1
        res = 0
        for key in hashNum:
            if key - 1 in hashNum:
                length = hashNum[key] + hashNum[key-1]
                if length > res:
                    res = length
        return res