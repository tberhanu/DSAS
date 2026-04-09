from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        start, end, all_ones_count = 0, 0, sum(nums)
        min_swap, once_count_so_far = len(nums), 0
        
        nums = nums * 2 # tricky: to avoid the circular array issue

        while end < len(nums):
            once_count_so_far += nums[end]
            window = end - start + 1
            if window < all_ones_count:
                end += 1
            else: # slide the window
                swap_needed = all_ones_count - once_count_so_far
                min_swap = min(min_swap, swap_needed)
                once_count_so_far -= nums[start]
                start += 1
                end += 1

        return min_swap


