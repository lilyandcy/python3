class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import itertools
        permutations = sorted(set(itertools.permutations(nums)))
        if tuple(nums) == permutations[-1]:
            nums[:] = list(permutations[0])
        else:
            nums[:] = list(permutations[permutations.index(tuple(nums))+1])