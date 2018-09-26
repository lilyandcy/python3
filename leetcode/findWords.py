class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        line2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
        rwords = []
        for w in words:
            l1 = 0
            l2 = 0
            l3 = 0
            for c in w:
                if c.upper() in line1:
                    l1 = 1
                else:
                    if c.upper() in line2:
                        l2 = 1
                    else:
                        l3 = 1
            if [l1, l2, l3].count(1) == 1:
                rwords.append(w)
        return rwords