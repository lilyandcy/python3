class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse = True)
        result = [deck[0]]
        for i in range(1, len(deck)):
            base = result[-1]
            del result[-1]
            result.insert(0, base)
            result.insert(0, deck[i])
        return result