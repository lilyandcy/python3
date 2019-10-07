class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        res = []
        for i in range(len(chips)):
            count = 0
            for j in range(len(chips)):
                if abs(chips[i]-chips[j]) & 1 == 1:
                    count += 1
            res.append(count)
        return min(res)