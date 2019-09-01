class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) < 4: return False
        a, b, c, (d, e, f) = 0, 0, 0, x[:3]
        for i in range(3, len(x)):
            a, b, c, d, e, f = b, c, d, e, f, x[i]
            if e < c - a and f >= d: return True
            if c - a <= e <= c and f >= (d if d - b < 0 else d - b): return True
        return False