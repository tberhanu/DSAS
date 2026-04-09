from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Note: first and last num are considered as adjacent (Tricky)
        """
        if len(nums) <= 2: return max(nums)
        return max(self.normalRob(nums[1:]), self.normalRob(nums[:-1])) # Tricky


    def normalRob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        left, right = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            best = max(left + nums[i], right)
            left = right
            right = best
        return best
        