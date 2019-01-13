class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(s)) == 1:
            return 1
        resStr = [0]
        subStr = ""
        ls = len(s)
        for i in range(ls-1):
            if ls - i > max(resStr):
                j = i + 1
                subStr = s[i]
                while j < ls:
                    subStr += s[j]
                    if len(set(subStr)) == len(subStr):
                        if len(subStr) > max(resStr):
                            resStr.append(len(subStr))
                        j += 1
                    else:
                        break
            else:
                break
        return max(resStr)