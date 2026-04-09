
# 34. Find First and Last Position of Element in Sorted Array
from bisect import bisect, bisect_left, bisect_right
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Inbuilt Binary Search
        bisect.bisect_left >> left most position to enter the target
        bisect.bisect_right >> right most position to enter the tartet

        Note: if the target is not found, then both will give us same index.
        """
        left_index = bisect.bisect_left(nums, target)
        right_index = bisect.bisect_right(nums, target)
        if left_index == right_index: # if target not found
            return [-1, -1]
        return [left_index, right_index - 1]