from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        nums = [2,5,6,0,0,1,2], target = 0 >> True
        nums = [2,5,6,0,0,1,2], target = 3 >> False
        [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4]

                        /
                    /
                / mid1
            /  
    start/ 
                                            /end
                                        /
                                    /mid2
                                /
                            /
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]: # left
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[end]: # right
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else: # either mid_val == start_val or mid_val == end_val (unknown direction)
                if nums[mid] == nums[start]:
                    start += 1
                else:
                    end -= 1
        
        return False
            
