class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # common code
        tempnum = nums1.copy()
        ltemp = 0
        inserted = 0
        for i in range(n):
            while nums2[i] >= tempnum[ltemp]:
                if ltemp < m + inserted:
                    ltemp = ltemp + 1
                else:
                    break
            tempnum.insert(ltemp, nums2[i])
            inserted = inserted + 1
            ltemp = ltemp + 1
        for i in range(m + n):
            nums1[i] = tempnum[i]