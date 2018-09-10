class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        reg = 0
        alist = []
        blist = []
        for c in a:
            alist.insert(0, c)
        for c in b:
            blist.insert(0, c)
        #print (alist)
        #print (blist)
        clist = []
        minl = min(len(alist), len(blist))
        for i in range(minl):
            if reg == 0:
                if int(alist[i]) + int(blist[i]) == 2:
                    reg = 1
                    clist.append("0")
                else:
                    result = int(alist[i]) + int(blist[i])
                    clist.append(str(result))
            else:
                if int(alist[i]) + int(blist[i]) == 2:
                    reg = 1
                    clist.append("1")
                else:
                    if int(alist[i]) + int(blist[i]) == 0:
                        reg = 0
                        clist.append("1")
                    else:
                        reg = 1
                        clist.append("0")
        if len(alist) > len(blist):
            for i in range(len(blist), len(alist)):
                if reg + int(alist[i]) == 2:
                    clist.append("0")
                else:
                    result = str(reg+int(alist[i]))
                    reg = 0
                    clist.append(result)
        else:
            for i in range(len(alist), len(blist)):
                if reg + int(blist[i]) == 2:
                    clist.append("0")
                else:
                    result = str(reg+int(blist[i]))
                    reg = 0
                    clist.append(result)
        if reg == 0:
            clist.reverse()
            return "".join(clist)
        else:
            clist.append("1")
            clist.reverse()
            return "".join(clist)