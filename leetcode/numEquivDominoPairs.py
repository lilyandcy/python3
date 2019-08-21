class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        d = collections.defaultdict(int)
        for i,j in dominoes:
            num = 10 * i + j if i < j else 10 * j + i
            res += d[num] # 原来num出现了几次，那么新加入1个num就能新组成几个匹配对
            d[num] += 1
        return res