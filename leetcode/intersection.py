class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        rlist = []
        if l1 < l2:
            for num in nums1:
                if num in nums2 and num not in rlist:
                    rlist.append(num)
        else:
            for num in nums2:
                if num in nums1 and num not in rlist:
                    rlist.append(num)
        return rlist