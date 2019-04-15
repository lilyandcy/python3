import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lenList = []
        for i in range(len(words)):
            lenList.append((words[i], len(words[i])))
        sortedList = sorted(lenList, key = lambda x: x[1], reverse = True)
        res = 0
        for comb in itertools.combinations(sortedList, 2):
            if not set(comb[0][0]) & set(comb[1][0]):
                if comb[0][1] * comb[1][1] > res:
                    res = comb[0][1] * comb[1][1]
        return res