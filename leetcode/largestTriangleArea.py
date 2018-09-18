class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        # p = (a + b + c)/2
        # S = (p * (p - a) * (p - b) * (p - c))**0.5
        # S = abs([x1(y2-y3) + x2(y3-y1) + x3(y1-y2)] * 0.5)
        rS = 0
        for i in range(len(points) - 2):
            for j in range(i+1, len(points) -1):
                for k in range(j+1, len(points)):
                    a = points[i][0] * (points[j][1] - points[k][1])
                    b = points[j][0] * (points[k][1] - points[i][1])
                    c = points[k][0] * (points[i][1] - points[j][1])
                    S = 0.5 * abs(a + b + c)
                    if S > rS:
                        rS = S
        return rS