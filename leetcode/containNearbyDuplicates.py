class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        list_len = len(nums)
        set_len = len(set(nums))
        if list_len == set_len:
            return False
        else:
            status = False
            for i in range(list_len-1):
                if nums.count(nums[i]) > 1:
                    for j in range(i+1, list_len):
                        if nums[i] == nums[j]:
                            if abs(i - j) <= k:
                                return True
            return False