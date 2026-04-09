class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dots, rows, cols, squares = [], defaultdict(set), defaultdict(set), defaultdict(set) # key = (r // 3, c // 3)
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    dots.append((r, c)) # very important to collect the DOTs to perform dfs later
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r // 3, c // 3)].add(val) # important

        index = 0
        def backtrack(index):
            if index == len(dots):
                return True

            r, c = dots[index]
            for i in range(1, 10): # very important
                num = str(i)
                if num in rows[r] or num in cols[c] or num in squares[(r // 3, c // 3)]:
                    continue
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)

                if backtrack(index + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                squares[(r // 3, c // 3)].remove(num)
            return False

        backtrack(index)



        