class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxSize = 0
        while l < r:
            size = (r - l) * min(height[l], height[r])
            if size > maxSize:
                maxSize = size
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxSize