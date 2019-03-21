class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        for i in range(26):
            c = chr(ord('a')+i)
            m = 101
            for ss in A:
                m = min(m,ss.count(c))
            res += m*[c]
        return res