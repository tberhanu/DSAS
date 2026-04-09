import math
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        [2,3,1,2,4,3]
        
        - start, end: keep END going until getting the target
        - need to shrink like start += 1
            as long as the total is >= target
            and keep update the min_window
        
        """
        start, end = 0, 0
        min_length, total = math.inf, 0

        while start <= end and end < len(nums):
            total += nums[end]
            if total >= target: # shrink
                min_length = min(min_length, end - start + 1)
                total = total - nums[start] - nums[end] # tricky
                start += 1
            else:
                end += 1

        return 0 if min_length == math.inf else min_length
