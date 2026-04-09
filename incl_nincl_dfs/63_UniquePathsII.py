class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        r, c, memo = 0, 0, {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if (r, c) == (ROWS - 1, COLS - 1) and obstacleGrid[r][c] == 0:
                return 1
            if (0 > r or r >= ROWS or 0 > c or c >= COLS or obstacleGrid[r][c] == 1):
                return 0
            
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)

            memo[(r, c)] = right + down
            return memo[(r, c)]
        
        return dfs(r, c)