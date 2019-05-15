class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) < 2:
            return asteroids
        right = []
        res = []
        for i in range(len(asteroids)):
            if asteroids[i] < 0 and right == []:
                res.append(asteroids[i])
            elif asteroids[i] < 0 and right != []:
                eliminated = 0
                while right != []:
                    if right[-1] + asteroids[i] > 0:
                        eliminated = 1
                        break
                    if right[-1] + asteroids[i] == 0:
                        eliminated = 1
                        right.pop()
                        break
                    if right[-1] + asteroids[i] < 0:
                        right.pop()
                if right == [] and eliminated == 0:
                    res.append(asteroids[i])
            else:
                right.append(asteroids[i])
        res.extend(right)
        return res