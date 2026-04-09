class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if matrix[r][c] == "0":
                memo[(r, c)] = 0
                return 0

            if matrix[r][c] == "1":
                memo[(r, c)] = 1 + min(dfs(r, c + 1), dfs(r + 1, c), dfs(r + 1, c + 1))
                return memo[(r, c)]


        max_square = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_square = max(max_square, dfs(r, c))
        
        return max_square ** 2