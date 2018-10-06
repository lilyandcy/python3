class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alist = a.split("+")
        blist = b.split("+")
        A = int(alist[0]) * int(blist[0]) - int(alist[1][0:-1]) * int(blist[1][0:-1])
        B = int(alist[0]) * int(blist[1][0:-1]) + int(blist[0]) * int(alist[1][0:-1])
        return str(A) + "+" + str(B) + "i"
