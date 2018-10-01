class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        rest = 0
        remain = 100
        dictChar = {}
        j = 0
        for i in range(ord("a"),ord("z") + 1):
            dictChar[chr(i)] = widths[j]
            j += 1
        for char in S:
            if remain < dictChar[char]:
                line += 1
                remain = 100 - dictChar[char]
                rest = dictChar[char]
            else:
                remain -= dictChar[char]
                rest += dictChar[char]
        return [line, rest]