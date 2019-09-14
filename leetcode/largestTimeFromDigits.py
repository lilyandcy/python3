from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        max_time = 0
        res = ''
        for ht, hb, mt, mb in permutations(A):
            hour, minute = ht * 10 + hb, mt * 10 + mb
            t = hour * 60 + minute
            if hour < 24 and minute < 60 and t >= max_time:
                res = "{}{}:{}{}".format(ht, hb, mt, mb)
                max_time = t
        return res