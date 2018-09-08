class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list_len = len(nums)
        set_len = len(set(nums))
        if list_len == set_len:
            return False
        else:
            return True