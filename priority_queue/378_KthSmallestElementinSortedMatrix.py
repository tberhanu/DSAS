
from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        since this is not linked list, we don't do: ll = ll.next, instead we
        increment the INDEX to track the current location

        """
        minHeap = []
        for lst in matrix:
            heapq.heappush(minHeap, (lst[0], 0, lst))
        
        count = 0
        while minHeap:
            val, index, lst = heapq.heappop(minHeap)
            count += 1
            if count == k:
                return val
            index += 1
            if index < len(lst):
                heapq.heappush(minHeap, (lst[index], index, lst))
        
