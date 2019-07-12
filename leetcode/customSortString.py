class Solution:
    def customSortString(self, S: str, T: str) -> str:
        mapT = {}
        for c in T:
            if c in mapT:
                mapT[c] += 1
            else:
                mapT[c] = 1
        ans = ""
        for c in S:
            if c in mapT:
                ans += c * mapT[c]
                mapT.pop(c)
        for key in mapT:
            ans += key * mapT[key]
        return ans