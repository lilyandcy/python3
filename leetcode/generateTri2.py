class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        List = []
        for i in range(rowIndex+1):
            sList = []
            for j in range(i+1):
                if j == 0 or j == i:
                   sList.append(1)
                else:
                    sList.append(List[j] + List[j-1])
            List = sList
        return sList