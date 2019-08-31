class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        sum = 0
        i = 1
        while True:
            sum += i
            if sum >= target and (sum-target) % 2 == 0:
                return i
            i += 1