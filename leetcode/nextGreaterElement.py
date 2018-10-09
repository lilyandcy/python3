class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rlist = []
        for num in nums1:
            index = nums2.index(num)
            found = False
            if index < len(nums2) - 1:
                for cnums in nums2[index+1:]:
                    if cnums > num:
                        rlist.append(cnums)
                        found = True
                        break
                if found == False:
                    rlist.append(-1)
            else:
                rlist.append(-1)
        return rlist