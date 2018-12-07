class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        length = 16
        res = ""
        lowPlate = licensePlate.lower()
        licenseDict = {}
        for char in lowPlate:
            if char.isalpha():
                if char not in licenseDict:
                    licenseDict[char] = 1
                else:
                    licenseDict[char] += 1
        for word in words:
            goodword = False
            for key in licenseDict:
                if key not in word:
                    goodword = False
                    break
                elif licenseDict[key] > word.count(key):
                    goodword = False
                    break
                else:
                    goodword = True
            if goodword == True:
                if len(word) < length:
                    res = word
                    length = len(word)
        return res