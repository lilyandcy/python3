import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        for comb in itertools.combinations(range(1,10), k):
            if sum(comb) == n:
                res.append(comb)
        return res