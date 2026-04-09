class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        O(log(m * n)) time complexity suggests Binary Search maybe the path.

        """
        ROWS, COLS = len(matrix), len(matrix[0])
        start, end = 0, (ROWS * COLS) - 1

        while start <= end:
            mid = start + (end - start) // 2
            row, col = mid // COLS, mid % COLS
            # row, col = mid // ROWS, mid % ROWS # if non-decreasing is based on ROWS, vertically
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                end = mid - 1
            else:
                start = mid + 1

        return False