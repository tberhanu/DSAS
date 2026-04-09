from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, sums = 0, sum(nums)
        for i, num in enumerate(nums):
            right_sum = sums - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1