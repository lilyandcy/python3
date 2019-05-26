class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(point1:List[int], point2:List[int]):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        p1p2 = distance(p1, p2)
        p2p3 = distance(p2, p3)
        p3p4 = distance(p3, p4)
        p1p4 = distance(p1, p4)
        p1p3 = distance(p1, p3)
        p2p4 = distance(p2, p4)
        lineL = [p1p2, p2p3,p3p4, p1p4, p1p3, p2p4]
        if lineL.count(p1p2) != 2 and lineL.count(p1p2) != 4:
            return False
        elif lineL.count(p1p2) == 4:
            for line in lineL:
                if line != p1p2 and line != 2 * p1p2:
                    return False
            return True
        else:
            for line in lineL:
                if line != p1p2 and line != p1p2 // 2:
                    return False
            return True
            