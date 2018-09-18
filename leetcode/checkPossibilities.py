class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible = 0
        j = 0
        # find count of pair of decreasing neighbors
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                j = i
                possible = possible + 1
        # no pair of neighbors decreasing
        if possible == 0:
            return True
        # larger than 1 pair of neighbor decreasing
        if possible > 1:
            return False
        # 4 conditions:
        # 4-1: First big
        # 4-2: Last small
        # 4-3: can decrease itself, i.e. 1,4,2,3
        # 4-4: can increase its neigbor, i.e. 1,4,2,5
        if j == 0 or j == len(nums) - 2 or nums[j-1] <= nums[j+1] or nums[j+2] >= nums[j]:
            return True
        return False