class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # judge whether to return 0
        if str == "" or str.count(" ") == len(str):
            return 0
        # get new str with first item not to be " "
        for i in range(len(str)):
            if str[i] != " ":
                index = i
                break
        newstr = str[i:]
        # first char is not a valid one
        if newstr[0] not in ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return 0
        # only have one char in the str
        if len(newstr) < 2:
            if newstr[0] == "+" or newstr[0] == "-" or newstr[0] == "0":
                return 0
            else:
                return int(newstr[0])
        if newstr[0] in ["+", "-"]:
            if newstr[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return 0
            else:
                for i in range(1, len(newstr)):
                    index = i
                    if newstr[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        break
                    index += 1
        else:
            # find first index not a numeric
            for i in range(len(newstr)):
                index = i
                if newstr[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    break
                index += 1
        integer = int(newstr[:index])
        if -2 ** 31 <= integer <= 2 ** 31 -1:
            return integer
        elif integer < -2 **31:
            return -2 ** 31
        else:
            return 2 ** 31 -1