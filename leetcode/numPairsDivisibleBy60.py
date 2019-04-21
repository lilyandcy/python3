class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ret = {}
        res = 0
        for i in range(len(time)):
            mod = time[i] % 60
            if mod != 0:
                needNum = 60 - mod
            else:
                needNum = 0
            if mod in ret:
                res += ret[mod]
            if needNum in ret:
                ret[needNum] += 1
            else:
                ret[needNum] = 1
        return res