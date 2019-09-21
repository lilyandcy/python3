class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dictB = {'a': 0, 'b': 0, 'o': 0, 'n': 0, 'l': 0}
        counto = 0
        countl = 0
        for c in text:
            if c == 'o' and counto == 0:
                counto += 1
            elif c == 'o' and counto == 1:
                dictB[c] += 1
                counto = 0
            if c == 'l' and countl == 0:
                countl += 1
            elif c == 'l' and countl == 1:
                dictB[c] += 1
                countl = 0
            if c == 'a' or c == 'b' or c == 'n':
                dictB[c] += 1
        return min(dictB.values())