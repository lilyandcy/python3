def commonSubstring(a, b):
        """
        :param a string List:
        :param b string List:
        :return print out "YES" or "NO":
        """
        length = len(a)
        for i in range(length):
            match = 0
            for j in range(len(a[i])):
                if a[i][j] in b[i]:
                    print("YES")
                    match = 1
                    break
            if match == 0:
                print("NO")

def countDuplicates(numbers):
        """
        :param numbers list(int):
        :return int:
        """
        numberSet = set(numbers)
        res = 0
        for num in numberSet:
            if numbers.count(num) > 1:
                res += 1
        return res

A = ["hello", "hix"]
B = ["world", "byedddx"]
commonSubstring(A, B)
C = [1,1,2,2,2,3,3]
print(countDuplicates(C))

