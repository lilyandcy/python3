import itertools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        length = len(t)
        count = 0
        for subStr in itertools.combinations(s,length):
            if t == "".join(list(subStr)):
                count += 1
        return count