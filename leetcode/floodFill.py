class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        origColor = image[sr][sc]
        image[sr][sc] = newColor
        if sr - 1 >= 0 and image[sr-1][sc] == origColor:
            self.floodFill(image, sr-1, sc, newColor)
        if sc - 1 >= 0 and image[sr][sc-1] == origColor:
            self.floodFill(image, sr, sc-1, newColor)
        if sr + 1 < len(image) and image[sr+1][sc] == origColor:
            self.floodFill(image, sr+1, sc, newColor)
        if sc + 1 < len(image[0]) and image[sr][sc+1] == origColor:
            self.floodFill(image, sr, sc+1, newColor)
        return image