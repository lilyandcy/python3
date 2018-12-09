class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        numlogs = []
        wordlogs = []
        for i in range(len(logs)):
            if logs[i][-1].isdigit():
                numlogs.append(logs[i])
            else:
                wordlogs.append(logs[i])
        wordlogs.sort(key = self.takeSecond)
        return wordlogs + numlogs

    def takeSecond(self, log):
        """
        :type log: str
        :rtype: str
        """
        i = log.find(" ")
        return log[i+1:]