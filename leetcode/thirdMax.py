class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setlist = set(nums)
        if len(setlist) < 3:
            return max(setlist)
        else:
            setlist.remove(max(setlist))
            setlist.remove(max(setlist))
            return max(setlist)