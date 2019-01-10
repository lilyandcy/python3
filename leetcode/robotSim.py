class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        # 0-N 1-E 2-S 3-W
        face = 0

        ObstacleSet = set(map(tuple, obstacles))
        print(ObstacleSet)

        x = 0
        y = 0
        MAX = 0
        for command in commands:
            if command == -2:
                face = (face + 3) % 4
            elif command == -1:
                face = (face + 1) % 4
            else:
                for i in range(command):
                    if (x + dx[face], y + dy[face]) in ObstacleSet:
                        break
                    else:
                        x = x + dx[face]
                        y = y + dy[face]
            MAX = max(MAX, x*x + y*y)
        return MAX