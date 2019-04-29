class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, dic = '', {}
        comp = {'w':'2','u':'4','g':'8','z':'0','x':'6','s':'7','v':'5','h':'3','o':'1','i':'9'}
        comp1 ={'w':'two','u':'four','g':'eight','z':'zero','x':'six','s':'seven','v':'five','h':'three','o':'one','i':'nine'}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for x, word in comp1.items():
            t = dic.get(x,0)
            if t > 0:
                res += comp[x] * t
                for w in word:
                    dic[w] -= t
        return ''.join(sorted(res))