class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        MIN = float('-inf')
        for num in nums[::-1]:
            if num < MIN:
                return True
            while stack and num > stack[-1]:
                MIN = stack.pop()
            stack.append(num)
        return False