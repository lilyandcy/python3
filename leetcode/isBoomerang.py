class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def distance(x1, x2, y1, y2):
            return ((x1-x2)**2+(y1-y2)**2)**0.5
        l01 = distance(points[0][0], points[1][0], points[0][1], points[1][1])
        l02 = distance(points[0][0], points[2][0], points[0][1], points[2][1])
        l12 = distance(points[1][0], points[2][0], points[1][1], points[2][1])
        print (l01, l02, l12)
        maxL = max(l01, max(l02, l12))
        print (maxL)
        if l01+l02+l12-maxL > maxL:
            return True
        return False