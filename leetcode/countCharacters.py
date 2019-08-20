class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        res = 0
        for char in chars:
            if char not in d.keys():
                d[char] = 1
            else:
                d[char] += 1
        for word in words:
            for c in word:
                if c not in d.keys() or word.count(c) > d[c]:
                    break
            else:
                res += len(word)
        return res