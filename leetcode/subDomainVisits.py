class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cpdict = {}
        rcpdomains = []
        for i in range(len(cpdomains)):
            count = int((cpdomains[i].split(" "))[0])
            urlstr = (cpdomains[i].split(" "))[1]
            urllist = urlstr.split(".")
            for j in range(len(urllist)):
                url = ".".join(urllist[j:])
                if url not in cpdict:
                    cpdict[url] = count
                else:
                    cpdict[url] += count
        for key in cpdict:
            rurl = ""
            rurl += str(cpdict[key])
            rurl += " "
            rurl += key
            rcpdomains.append(rurl)
        return rcpdomains