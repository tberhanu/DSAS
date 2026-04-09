
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [2,       3,         -2,            4]
        (2,2)   (6,3).    (-12,-2)  (-48,4)

        """
        max_prod, min_prod, largest = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i] * max_prod, nums[i] * min_prod, nums[i])
            cur_min = min(nums[i] * max_prod, nums[i] * min_prod, nums[i])
            max_prod, min_prod = cur_max, cur_min
            largest = max(largest, max_prod)
        return largest