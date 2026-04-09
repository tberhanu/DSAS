class NumArray: # 303

    def __init__(self, nums: List[int]):
        self.prefix = nums[:]
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i] + self.prefix[i - 1]
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



class NumMatrix: # 304
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        self.dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)] # Very Important to handle edge cases
        
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                self.dp[r][c] = self.matrix[r - 1][c - 1] \
                                + self.dp[r][c - 1] \
                                + self.dp[r - 1][c] \
                                - self.dp[r - 1][c - 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bigger_region = self.dp[row2][col2]
        upperTop_region = self.dp[row1 - 1][col2]
        leftSide_region = self.dp[row2][col1 - 1]
        intersection_region = self.dp[row1 - 1][col1 - 1]

        target_region = bigger_region - upperTop_region - leftSide_region
        target_region = target_region + intersection_region # removing dup operation

        return target_region

        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)