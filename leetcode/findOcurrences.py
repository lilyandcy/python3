class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        if not text:
            return res

        regex = first + " " + second + " "
        temp = text.split(regex, 1)
        while len(temp) > 1:
            s = temp[1].split(" ")[0]
            if s:
                res.append(s)
            text = temp[1]
            temp = text.split(regex, 1)
        return res