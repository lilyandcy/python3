class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senateList = []
        for i in range(len(senate)):
            senateList.append(senate[i])
        i = 0
        while i < len(senateList):
            if senateList.count("R") == 0:
                return "Dire"
            if senateList.count("D") == 0:
                return "Radiant"
            if i == len(senateList) - 1:
                if senateList[i] == "R":
                    senateList[senateList.index("D")] = "X"
                elif senateList[i] == "D":
                    senateList[senateList.index("R")] = "X"
                i = 0
            else:
                if senateList[i] == "R":
                    if "D" in senateList[i+1:]:
                        senateList[senateList[i+1:].index("D")+i+1] = "X"
                    else:
                        senateList[senateList.index("D")] = "X"
                elif senateList[i] == "D":
                    if "R" in senateList[i+1:]:
                        senateList[senateList[i+1:].index("R")+i+1] = "X"
                    else:
                        senateList[senateList.index("R")] = "X"
                i += 1
