class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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

