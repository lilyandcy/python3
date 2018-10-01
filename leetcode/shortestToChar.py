class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distance = []
        baseIndex = S.find(C)
        for i in range(len(S)):
            if i < baseIndex:
                distance.append(abs(baseIndex - i))
            elif i == baseIndex:
                distance.append(0)
            else:
                newIndex = S.find(C, i, len(S))
                if newIndex == -1:
                    distance.append(abs(baseIndex - i))
                else:
                    if abs(newIndex - i) < abs(baseIndex - i):
                        distance.append(abs(newIndex - i))
                        baseIndex = newIndex
                    else:
                        distance.append(abs(baseIndex - i))
        return distance