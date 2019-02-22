class Solution:
    def computeArea(self, A: 'int', B: 'int', C: 'int', D: 'int', E: 'int', F: 'int', G: 'int', H: 'int') -> 'int':
        s1 = (D-B) * (C-A)
        s2 = (H-F) * (G-E)
        if C>=G and D>=H and E>=A and F>=B:
            return s1
        if G>=C and H>=D and A>=E and B>=F:
            return s2
        if E>=C or A>=G or F>=D or B>=H:
            return s1+s2

        wid1 = min(C-E, G-A)
        wid2 = min(C-A, G-E)
        wid = min(wid1, wid2)
        hei1 = min(D-F, H-B)
        hei2 = min(D-B, H-F)
        hei = min(hei1, hei2)
        return s1+s2-wid*hei