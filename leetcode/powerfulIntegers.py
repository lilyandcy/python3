class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = set()
        for i in range(18):
            for j in range(18):
                v = x ** i + y ** j
                if v <= bound:
                    res.add(v)
        return list(res)