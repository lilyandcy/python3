class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-','').upper()
        length = len(S)
        head = length % K
        r = []
        if head == 0:
            for n in range(length // K):
                r.append(S[n*K:(n+1)*K])
            return '-'.join(r)
        else:
            r.append(S[:head])
            for n in range((length-head)//K):
                r.append(S[head+n*K:head+(n+1)*K])
            return '-'.join(r)