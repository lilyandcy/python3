class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rlist = []
        for i in range(1, n+1):
            if i % 15 == 0:
                rlist.append("FizzBuzz")
            else:
                if i % 3 == 0:
                    rlist.append("Fizz")
                else:
                    if i % 5 == 0:
                        rlist.append("Buzz")
                    else:
                        rlist.append(str(i))
        return rlist