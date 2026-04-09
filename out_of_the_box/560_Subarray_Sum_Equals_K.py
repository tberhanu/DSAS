from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        nums = [ 1, 2,  3, 1, 1, 1, 2], k = 3 >> (1, 2), (3), (1, 1, 1), (1, 2) >> result = 4
        sums  0, 1, 3, 6, 7, 8, 9, 11
                    *. *        *.  *
        corner case: nums = [1, -1, 0], k = 0 >> (1, -1), (-1, 0), (1, -1, 0) >> result = 3
        
        """

        sum_to_counts = defaultdict(int)
        count, total = 0, 0
        for i, num in enumerate(nums):
            total += num
            if total == k:
                count += 1
                
            count += sum_to_counts[total - k]
            
            sum_to_counts[total] += 1

        return count