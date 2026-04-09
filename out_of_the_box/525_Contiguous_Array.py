from typing import List, Optional

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        zeroes, ones = 0, 0

        nums =           [0,   1,    1,    1,    1,    1,     0,     0,    0]
        (zeroes, ones) = (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(2,5),(3,5),(4,5)

        """
        diff_to_index = {}
        zeroes, ones = 0, 0
        longest = 0
        for index, num in enumerate(nums):
            if num == 0: zeroes += 1
            if num == 1: ones += 1

            diff = zeroes - ones
            if diff == 0:
                longest = max(longest, zeroes + ones)
                continue
            else:
                if diff not in diff_to_index:
                    diff_to_index[diff] = index
                else:
                    prev_index = diff_to_index[diff]
                    longest = max(longest, index - prev_index)
        return longest
                    
            
