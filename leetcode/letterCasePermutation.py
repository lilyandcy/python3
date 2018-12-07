class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        cur_s =[S]
        for i in range(len(S)):
            next_s = []
            for s in cur_s:
                if s[i].isdigit():
                    next_s.append(s)
                else:
                    next_s.append(s[0:i] + s[i].lower() + s[i + 1:])
                    next_s.append(s[0:i] + s[i].upper() + s[i + 1:])
            cur_s = next_s
        return cur_s