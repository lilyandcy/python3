class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res, queries_count, words_count = [], [], []
        for w in words:
            words_count.append(w.count(min(w)))
        for q in queries:
            c = q.count(min(q))
            # 在 words_count 里数一下有多少是比 c 大的
            res.append(len([x for x in words_count if c < x]))
        return res
