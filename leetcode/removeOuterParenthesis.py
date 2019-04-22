class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        primitive = ''
        s = ''
        count = 0
        for i in range(len(S)):
            s += S[i]
            if S[i] == '(':
                count += 1
            elif S[i] == ')':
                count -= 1
            if count == 0:
                primitive += s[1:-1]
                s = ''
        return primitive