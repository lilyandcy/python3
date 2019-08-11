class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        if length == 1:
            return [0]
        res = [0]
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if T[i] < T[j]:
                    res.append(j-i)
                    break
                elif T[i] >= T[j] and j == length - 1:
                    res.append(0)
                    break
        res.reverse()
        return res