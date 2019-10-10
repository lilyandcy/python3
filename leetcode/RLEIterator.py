class RLEIterator:

    def __init__(self, A: List[int]):
        self.arr = []
        self.count = 0
        for i, n in enumerate(A):
            if i%2 == 1:
                continue
            self.arr.append([A[i+1], n])
            self.count += n

    def next(self, n: int) -> int:
        arr = self.arr
        res = -1
        while n > 0:
            if self.count <= 0:
                return -1
            num = arr[0][0]
            le = arr[0][1]
            if n <= le:
                res = num
                arr[0][1] -= n
                self.count -= n
                if n == le:
                    arr.pop(0)
                n = 0
            else:
                n -= le
                self.count -= le
                arr.pop(0)
        return res


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)