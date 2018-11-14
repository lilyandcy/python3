class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 3:
            return 0
        dVector = []
        for i in range(len(points)):
            dList = {}
            for j in range(len(points)):
                distance = self.pointDistance(points[i], points[j])
                if i != j:
                    if dList.get(distance) == None:
                        dList[distance] = 1
                    else:
                        dList[distance] += 1
            dVector.append(dList)
        count = 0
        for i in range(len(dVector)):
            for n in dVector[i].values():
                if n > 1:
                    count += n * (n - 1)
        return count


    def pointDistance(self, x, y):
        """
        :type x, y: List[inta, intb]
        :rtype: float
        """
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2