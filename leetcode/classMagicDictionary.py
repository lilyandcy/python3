class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.dict = dict


    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        self.list = list()
        n = len(word)
        for k in self.dict:
            if len(k) == n:
                self.list.append(k)
        for k in self.list:
            p = 0
            for i in range(n):
                if k[i] != word[i]:
                    p += 1
            if p == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)