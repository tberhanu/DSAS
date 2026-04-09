
from typing import List
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        priority queue by freq, maxHeap
            when in tie, use decreasing order of the num itelf

        """
        minHeap, lookup_freq, results = [], Counter(nums), []
        for num, freq in lookup_freq.items():
            heapq.heappush(minHeap, (freq, -num))

        while minHeap:
            freq, num = heapq.heappop(minHeap)
            result = [-num] * freq
            results.extend(result)
        return results
