import itertools
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        for i in range(1, len(candidates)+1):
            for comb in itertools.combinations(candidates, i):
                if sum(list(comb)) == target and list(comb) not in res:
                    res.append(list(comb))
        return res