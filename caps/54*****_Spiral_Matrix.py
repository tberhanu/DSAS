class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        (0,0), (0,1) .... (0,C)
                           (1,C)....(R,C)
                                    (R,C-1),(R,C-2),(R,C-3)...(R,0)
                                                              (R-1,0),(R-2,0)....(1,0)
        1. increment cols
        2. increment rows
        3. decrement cols
        4. decrement rows

        """
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # collect the top row
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1
            # collect the right col
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])
            right -= 1
            # since we alter TOP and RIGHT, need to verify if our condition still there
            if not (left < right and top < bottom):
                break
            # collect the bottom row
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][col])
            bottom -= 1
            # collect the left col
            for row in range(bottom - 1, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
        
        return result