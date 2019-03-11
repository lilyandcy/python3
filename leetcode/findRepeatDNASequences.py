class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        res = []
        for i in range(len(s)-10):
            baseStr = s[i:i+10]
            if s.find(baseStr, i+1) != -1:
                res.append(baseStr)
        return list(set(res))