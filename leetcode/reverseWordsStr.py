class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        strList = []
        for i in range(len(sList)):
            if sList[i] != "":
                strList.append(sList[i])
        return " ".join(strList[::-1])