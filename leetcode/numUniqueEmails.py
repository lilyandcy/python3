class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        lenM = len(emails)
        if lenM < 1:
            return 0
        if lenM < 2:
            return 1
        res = 0
        emailL = []
        for email in emails:
            temp = email.split("@")
            domain = temp[1]
            prefix = temp[0][:temp[0].find("+")].replace(".","")
            newemail = prefix + "@" + domain
            if newemail not in emailL:
                res += 1
                emailL.append(newemail)
        return res