from math import sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        solution lies between 1 and sqrt(num) so binary searching the range is good idea

        """
        start, end = 1, sqrt(num)
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                end = mid - 1
            if mid * mid < num:
                start = mid + 1
        return False