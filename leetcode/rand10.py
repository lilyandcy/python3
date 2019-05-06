# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()

        if a > 4 and b < 4:
            return self.rand10()
        else:
            return (a+b) % 10 + 1