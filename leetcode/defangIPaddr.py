class Solution:
    def defangIPaddr(self, address: str) -> str:
        ipList = address.split('.')
        res = ''
        for ip in ipList:
            res += ip + '[.]'
        return res[:-3]