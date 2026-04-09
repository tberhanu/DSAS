from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        nums = [5,6,7,8,9,0,1,2,3,4] , in O(log n) times
        corner cases:
            [2], single num
            [0,1,2,4,5,6,7], min at first, not rotated, increasing order
            [1,2,4,5,6,7,0], min at end
        
        To make life easy, check if nums not rotated, and return nums[0]

        """
            
        if len(nums) == 1: # if only one num
            return nums[0]
        if nums[0] < nums[-1]: # if min at first
            return nums[0]
        if nums[-2] >= nums[-1] <= nums[0]: # if min at last
            return nums[-1]
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[start] <= nums[mid]: # got to the right
                start = mid
            elif nums[mid] <= nums[end]: # to to the left
                end = mid
        