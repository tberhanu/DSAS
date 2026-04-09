from math import ceil

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        solution lies between 0 to x//2, so binary searching the range is good idea
        0,1,2,3,4,5,6,7,8
        how we take care the decimal fractions ?
        """
        # ceil is just if x = 1 (we can handle 0 and 1 as special cases)
        start, end = 0, ceil(x / 2) 
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                if (mid - 1) * (mid - 1) < x:
                    return mid - 1
                end = mid - 1
            if mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                start = mid + 1
