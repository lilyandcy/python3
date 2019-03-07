class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        arrayNum = int("".join(str(i) for i in A))
        res = list(int(i) for i in str(arrayNum + K))
        return res