class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = list(name)
        t = list(typed)
        i, j = 0, 0
        while n and t:
            if n[0] == t[0]:
                n.pop(0)
                t.pop(0)
            else:
                t.pop(0)
        if not n and not t:
            return True
        if n:
            return False
        if t:
            return True