class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stackMark = []
        for c in ops:
            if c == "C":
                stackMark.pop()
            elif c == "D":
                score = stackMark[-1] * 2
                stackMark.append(score)
            elif c == "+":
                score = stackMark[-1] + stackMark[-2]
                stackMark.append(score)
            else:
                stackMark.append(int(c))
        return sum(stackMark)