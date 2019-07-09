class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = collections.Counter(answers)
        ans = 0
        for i in c:
            ans += math.ceil(c[i]/(i+1))*(i+1)
        return ans