class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        print (s)
        res = []
        for x in s:
            if not x:
                continue
            elif x == '..':
                if res:
                    res.pop()
                else:
                    continue
            elif not x == '.':
                res.append(x)
        return '/' + '/'.join(res)