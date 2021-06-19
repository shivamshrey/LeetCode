# 733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j, newColor, originalColor):
            if i < 0 or i >= len(image) \
                or j < 0 or j >= len(image[0]) \
                or image[i][j] != originalColor \
                or image[i][j] == newColor:
                return
            
            image[i][j] = newColor
            
            dfs(i - 1, j, newColor, originalColor)
            dfs(i, j - 1, newColor, originalColor)
            dfs(i, j + 1, newColor, originalColor)
            dfs(i + 1, j, newColor, originalColor)
            
        originalColor = image[sr][sc]
        dfs(sr, sc, newColor, originalColor)
        return image
    