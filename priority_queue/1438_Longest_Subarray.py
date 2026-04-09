
from typing import List

import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        [1,5,6,7,8,10,6,5,6], limit = 4
        1. traverse thru nums, add (elt, index) to minHeap and maxHeap
        2. if diff of maxHeap[0] and minHeap[0] <= limit, keep going while updating longest_window
        3. if not: shrink the window START from the MIN INDEX of maxHeap[0] and minHeap[0]
        4. tricky: 

        """
        minHeap, maxHeap, longest, start = [], [], 0, 0
        for end in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[end], end))
            heapq.heappush(minHeap, (nums[end], end))
            while -maxHeap[0][0] - minHeap[0][0] > limit: # time to shrink the window size
                index = min(maxHeap[0][1], minHeap[0][1])
                start = index + 1 # moving our START forward, sliding window
                # need to remove all at INDEX AND less than INDEX
                while maxHeap[0][1] < start:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < start:
                    heapq.heappop(minHeap)

            longest = max(longest, end - start + 1)

        return longest



class Solution2: # Time Limit Exceeded.   56 / 63 testcases passed
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Brute force
        
        """
        i, maxCount = 0, 0
        while i < len(nums):
            j, count = i, 0
            maxx, minn = nums[i], nums[j]
            while j < len(nums):
                maxx = max(maxx, nums[j])
                minn = min(minn, nums[j])
                if abs(maxx - minn) <= limit:
                    count += 1
                    maxCount = max(maxCount, count)
                    j += 1
                else:
                    break
            i += 1
        return maxCount