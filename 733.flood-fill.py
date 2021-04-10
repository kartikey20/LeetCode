#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        colorToChange = image[sr][sc]
        rows = len(image)
        cols= len(image[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or image[r][c] == newColor or image[r][c] != colorToChange:
                return
            image[r][c] = newColor
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image

        
# @lc code=end

