class Solution: # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        seen, count = set(), 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    seen.add((r, c))
                    continue
                if (r, c) not in seen:
                    self.dfs(r, c, seen, grid)
                    count += 1

        return count


    def dfs(self, r, c, seen, grid):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 
        if (r, c) in seen:
            return
        if grid[r][c] == "0":
            seen.add((r, c))
            return
        
        seen.add((r, c))

        self.dfs(r, c - 1, seen, grid) # left
        self.dfs(r, c + 1, seen, grid) # right
        self.dfs(r - 1, c, seen, grid) # up
        self.dfs(r + 1, c, seen, grid) # down





class Solution2: # BFS
    def numIslands2(self, grid: List[List[str]]) -> int:
        """
        1. double for loop: BFS with seen
            2. once queue is empty: count ++
        3. if Index Out, ignore it


        """
        seen, count = set(), 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen:
                    seen.add((r, c))
                    if grid[r][c] == "1":
                        self.mark_island_as_seen_bfs(r, c, seen, grid) # trick: seen is object passed by REFERENCE
                        count += 1
        return count

    def mark_island_as_seen_bfs(self, r, c, seen, grid):
        queue = deque()
        queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for row, col in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                ROWS, COLS = len(grid), len(grid[0])
                if self.is_valid(row, col, ROWS, COLS) and (row, col) not in seen:
                    seen.add((row, col)) # mark as seen both for "1" and "0", so box with "0" will be skipped in the double for loop
                    if grid[row][col] == "1": # only add to queue if it's "1", so we only conitnue BFS for "1"
                        queue.append((row, col))
        

    def is_valid(self, row, col, ROWS, COLS):
        return row >= 0 and col >= 0 and row < ROWS and col < COLS       

