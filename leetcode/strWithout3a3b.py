class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        a, b = 'a', 'b'
        if A > B:
            a, b = b, a
            A, B = B, A
        if 2*A > B:
            return (b+b+a)*(B-A) + (b+a)*(2*A-B)
        else:
            return (b+b+a)*A + b*(B-2*A)