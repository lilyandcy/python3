class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = {}
        for i in range(len(deck)):
            if deck[i]  in d:
                d[deck[i]] += 1
            else:
                d[deck[i]] = 1
        gcd = d[deck[0]]
        num = set(d.values())

        for i in num:
            gcd = find_gcd(gcd, i)
        if gcd == 1:
            return False
        else:
            return True

def find_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a