class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        res = []
        dic = {}
        for i in range(len(s)-9):
            temp = s[i:i+10]
            dic[temp] = dic.get(temp, 0) + 1
            if dic[temp] == 2:
                res.append(temp)
        return res