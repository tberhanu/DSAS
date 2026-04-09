from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i, seen):
            
            if r < 0 or c < 0 or r >= len(board) or \
               c >= len(board[0]) or (r, c) in seen:
                return False

            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            if board[r][c] != word[i]:
                return False

            seen.add((r, c)) # tricky

            up, right, left = False, False, False
            down = dfs(r + 1, c, i + 1, seen)
            if not down:
                up = dfs(r - 1, c, i + 1, seen)
                if not up:
                    right = dfs(r, c + 1, i + 1, seen)
                    if not right:
                        left = dfs(r, c - 1, i + 1, seen)

            seen.remove((r, c)) # tricky

            return down or up or right or left

        for row in range(len(board)):
            for col in range(len(board[0])):
                seen = set()
                if dfs(row, col, 0, seen):
                    return True
        return False

        