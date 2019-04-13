import itertools
class Solution:
    def countArrangement(self, N: int) -> int:
        listN = []
        res = 0
        for i in range(1, N+1):
            listN.append(i)
        for perm in itertools.permutations(listN, N):
            flag = 0
            for j in range(N):
                if perm[j] % (j+1) != 0 and (j+1) % perm[j] != 0:
                    flag = 1
                    break
            if flag == 0:
                res += 1
        return res