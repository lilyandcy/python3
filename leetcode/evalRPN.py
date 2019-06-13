class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
                continue
            if token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
                continue
            if token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
                continue
            if token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                num = num2 // num1
                if num < 0 and num2 % num1 != 0:
                    num += 1
                stack.append(num)
                continue
            stack.append(int(token))
        return stack.pop()