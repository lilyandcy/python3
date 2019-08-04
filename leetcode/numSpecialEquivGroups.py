class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for sub in A:
            sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(sub)
        return len(res)