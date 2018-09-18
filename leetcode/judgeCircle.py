class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves == "":
            return True
        if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
            return True
        return False