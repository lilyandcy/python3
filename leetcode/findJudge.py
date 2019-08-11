class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge = []
        for i in range(N):
            judge.append([0,0])
        for i in range(len(trust)):
            judge[trust[i][0]-1][0] += 1
            judge[trust[i][1]-1][1] += 1
        for j in range(len(judge)):
            if judge[j][0] == 0 and judge[j][1] == N-1:
                return j+1
        return -1
    # pre-check-in