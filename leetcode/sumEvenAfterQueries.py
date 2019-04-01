class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        res = []
        evenSum = 0
        for num in A:
            if num % 2 == 0:
                evenSum += num
        for i in range(len(queries)):
            index = queries[i][1]
            val = queries[i][0]
            # both val and indexNum are even, increase evenSum with val, update indexNum and res
            if val % 2 == 0 and A[index] % 2 == 0:
                evenSum += val
                A[index] += val
                res.append(evenSum)
            # val is even, indexNum is odd, nothing, update indexNum and res
            elif val % 2 == 0 and A[index] % 2 != 0:
                A[index] += val
                res.append(evenSum)
            # val is odd, indexNum is even, decrease evenSum with indexNum, update indexNum and res
            elif val % 2 != 0 and A[index] % 2 == 0:
                evenSum -= A[index]
                A[index] += val
                res.append(evenSum)
            # both val and indexNum is odd, increase evenSum with val+indexNum, update indexNum and res
            else:
                evenSum += val+A[index]
                A[index] += val
                res.append(evenSum)
        return res
