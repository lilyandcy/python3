class Solution:
    def dayOfYear(self, date: str) -> int:
        normalYear = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        unYear = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        res = 0
        listDate = date.split('-')
        if int(listDate[0]) % 4 == 0 and listDate[0] != '1900':
            if listDate[1] not in ["10", "11", "12"]:
                MM = int(listDate[1][1])
                for i in range(1, MM):
                    res += unYear[i]
                if listDate[2]  not in ["01", "02", "03", "04", "05", "06", "07", "08", "09"]:
                    res += int(listDate[2])
                else:
                    res += int(listDate[2][1])
            else:
                MM = int(listDate[1])
                for i in range(1, MM):
                    res += unYear[i]
                if listDate[2]  not in ["01", "02", "03", "04", "05", "06", "07", "08", "09"]:
                    res += int(listDate[2])
                else:
                    res += int(listDate[2][1])
        else:
            if listDate[1] not in ["10", "11", "12"]:
                MM = int(listDate[1][1])
                for i in range(1, MM):
                    res += normalYear[i]
                if listDate[2]  not in ["01", "02", "03", "04", "05", "06", "07", "08", "09"]:
                    res += int(listDate[2])
                else:
                    res += int(listDate[2][1])
            else:
                MM = int(listDate[1])
                for i in range(1, MM):
                    res += normalYear[i]
                if listDate[2]  not in ["01", "02", "03", "04", "05", "06", "07", "08", "09"]:
                    res += int(listDate[2])
                else:
                    res += int(listDate[2][1])
        return res