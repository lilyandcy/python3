class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        temp = [x.split(',') for x in transactions]
        for idx1, cont1 in enumerate(transactions):
            if int(temp[idx1][2]) > 1000:
                res.append(cont1)
                continue
            for idx2, cont2 in enumerate(transactions):
                if idx2 == idx1:
                    continue
                if temp[idx1][0] == temp[idx2][0] and temp[idx1][3] != temp[idx2][3] and abs(int(temp[idx1][1]) - int(temp[idx2][1])) <= 60:
                    res.append(cont1)
                    break
        return res