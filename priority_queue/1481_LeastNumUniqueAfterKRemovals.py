
from typing import List
from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        arr = [5,5,4], k = 1 >> [5]
        
        1. need ordered by freq >> priority queue
        2. pop the least freq as long as you have enough K  
        

        """
        counter, minHeap = Counter(arr), []
        for num, freq in counter.items():
            heapq.heappush(minHeap, (freq, num))

        while minHeap and k >= minHeap[0][0]:
            freq, num = heapq.heappop(minHeap)
            k = k - freq


        return len(minHeap)

