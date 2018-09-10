class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ws = ""
        wlist = []
        for i in range(len(s)):
            if s[i] != " ":
                ws = ws + s[i]
            else:
                if ws != "":
                    wlist.append(ws)
                    ws = ""
        if ws != "":
            wlist.append(ws)
        return len(wlist)