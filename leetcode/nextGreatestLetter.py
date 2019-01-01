class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        length = len(letters)
        if letters[length - 1] <= target:
            return letters[0]
        for letter in letters:
            if letter > target:
                return letter