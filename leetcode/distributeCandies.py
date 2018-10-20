class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        setCandies = set(candies)
        if len(setCandies) >= len(candies) // 2:
            return len(candies) // 2
        else:
            return len(setCandies)