from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lpara = paragraph.lower()
        words = re.findall(r'[a-z]+', lpara)
        count = Counter(words)
        res = count.most_common(len(banned) + 1)
        for key in res:
            if key[0] not in banned:
                return key[0]