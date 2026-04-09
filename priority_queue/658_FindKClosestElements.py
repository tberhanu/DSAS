
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        heapq: use key=abs(num - x) for priority and then key2=num in case of tie
        heapq.nsmallest(k, minHeap)
        No need to heapify as heapq.nsmallest do it internally

        """
        arr = [(abs(num - x), num) for num in arr]
        
        lst = heapq.nsmallest(k, arr)
        result = [num for diff, num in lst]

        return sorted(result)