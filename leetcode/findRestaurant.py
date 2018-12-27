class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        resR = []
        for i in range(len(list1)):
            if list1[i] in list2:
                res.append((i, list2.index(list1[i])))
        minValue = sum(min(res))
        for i in range(len(res)):
            if sum(res[i]) == minValue:
                resR.append(list1[res[i][0]])
        return resR