class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def distance(point):
            """
            :type point: List[int]
            :rtype: float
            """
            return (point[0]**2 + point[1]**2)
        return sorted(points, key=lambda x: distance(x))[:K]