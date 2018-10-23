class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = area
        W = 1
        wl = [L, W]
        while W <= L:
            if area % W == 0:
                L = area // W
                wl[0], wl[1] = L, W
                W += 1
            else:
                W += 1
            L = area // W
        return wl