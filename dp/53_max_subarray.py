
import heapq
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                 =
                 =. =
                 =. =. =
                [-2, 1, -2, 4, 3, 5, 6, 1, 5]
        dp[i] = max(dp[i - 1], nums[i], nums[i])
        """
        largest_sum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            largest_sum = max(largest_sum, nums[i])
        
        return largest_sum