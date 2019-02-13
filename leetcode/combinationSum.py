class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def temp(yiyou,t,cand):
            if t in cand:
                res.append(yiyou+[t])
            if t > cand[0]:
                for i in range(len(cand)):
                    temp(yiyou+[cand[i]], t-cand[i], cand[i:])
        temp([],target,candidates)
        return res