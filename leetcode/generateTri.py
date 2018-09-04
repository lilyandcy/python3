class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        List = []
        for i in range(numRows):
            sList = []
            for j in range(i+1):
                if j == 0 or j == i:
                   sList.append(1)
                else:
                    sList.append(List[i-1][j] + List[i-1][j-1])
            print (sList)
            List.append(sList)
        return List