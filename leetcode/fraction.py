class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        i = len(cont) - 1
        nume = cont[i]
        deno = 1
        while i > 0:
            inter = nume
            nume = deno
            deno = inter
            nume += deno * cont[i-1]
            i -= 1
        return [nume, deno]