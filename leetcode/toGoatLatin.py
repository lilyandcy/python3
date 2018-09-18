class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowelset = {"a","e","i","o","u","A","E","I","O","U"}
        Slist = S.split(" ")
        for i in range(len(Slist)):
            #first char is vowel
            if Slist[i][0] in vowelset:
                Slist[i] += "ma"
            else:
                Slist[i] = Slist[i][1:] + Slist[i][0] + "ma"
            tailstr = ""
            for j in range(i+1):
                tailstr += "a"
            Slist[i] += tailstr
        return " ".join(Slist)