class Solution:
    def frequencySort(self, s: str) -> str:
        mapString = {}
        res = ""
        for c in s:
            if c not in mapString:
                mapString[c] = s.count(c)
        length = len(mapString)
        while length > 0:
            maxKey = max(mapString, key = mapString.get)
            count = mapString[maxKey]
            while count > 0:
                res += maxKey
                count -= 1
            mapString.pop(maxKey)
            length -= 1
        return res