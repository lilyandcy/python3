class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                stack.append(c)
            else:
                if c == "/":
                    c = "//"
                right = stack.pop()
                left = stack.pop()
                res = eval(str(left) + c + str(right))
                stack.append(res)
        return stack.pop()